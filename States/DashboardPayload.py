from States.GameState import GameState
from Engines.MonteCarloEngine import MonteCarloEngine
from Data.location_data import compute_theater_metrics


class DashboardPayloadBuilder:
    """
    Builds a front-end-ready payload for the selected season and all country histories.
    """

    @staticmethod
    def build(game_timeline, year, season):
        summary = game_timeline.get_season_summary(year, season)
        payload = {
            "selectedSeason": {"year": year, "season": season},
            "availableSeasons": [],
            "countries": {},
            "forecast": {},
        }

        board = game_timeline.get_board(year, season)

        seasons = set()
        for country, state in summary.items():
            seasons.add((state.year, state.season))

        for country, timeline in game_timeline.country_timelines.items():
            for snapshot in timeline.snapshots:
                seasons.add((snapshot.year, snapshot.season))

        payload["availableSeasons"] = [
            {"year": year_value, "season": season_name}
            for year_value, season_name in sorted(seasons, key=lambda item: (item[0], ["Spring", "Summer", "Fall", "Winter"].index(item[1]) if item[1] in ["Spring", "Summer", "Fall", "Winter"] else 99))
        ]

        if board:
            for country, state in summary.items():
                state.sc = len([province for province, owner in board.sc_owners.items() if owner == country])
                state.units = len([unit for unit in board.units_by_province.values() if unit.country == country])

        for country, state in summary.items():
            timeline = game_timeline.get_country_timeline(country)
            history = []
            if timeline:
                for snapshot in timeline.snapshots:
                    history.append({
                        "year": snapshot.year,
                        "season": snapshot.season,
                        **snapshot.country_state.__dict__,
                    })

            payload["countries"][country] = {
                "current": state.__dict__.copy(),
                "history": history,
            }

        game_state = GameState(year, season)
        if board:
            game_state.board = board
            for unit in board.units_by_province.values():
                game_state.board.add_unit(unit)
            for province, owner in board.sc_owners.items():
                game_state.board.sc_owners[province] = owner
        for country, data in payload["countries"].items():
            state = data["current"]
            from States.CountryState import CountryState
            game_state.add_country_state(CountryState(
                country=state["country"],
                year=state["year"],
                season=state["season"],
                sc=state.get("sc", 0),
                units=state.get("units", 0),
                builds=state.get("builds", 0),
            ))

            game_state.countries[country].__dict__.update(state)

        forecast_engine = MonteCarloEngine()
        if board and board.units_by_province:
            payload["forecastDetails"] = forecast_engine.simulate_trials(game_state, iterations=400)
            payload["forecast"] = {
                country: details["win_probability"]
                for country, details in payload["forecastDetails"]["countries"].items()
            }
        else:
            payload["forecast"] = forecast_engine.simulate(game_state, iterations=400)
            payload["forecastDetails"] = {
                "countries": {},
                "draw_probability": 0.0,
                "terminal_reasons": {},
            }
        for country, probability in payload["forecast"].items():
            if country in payload["countries"]:
                payload["countries"][country]["current"]["forecast_score"] = probability
                payload["countries"][country]["current"]["win_probability"] = probability

        payload["board"] = {
            "units": [
                {
                    "country": unit.country,
                    "unit_type": unit.unit_type,
                    "province": unit.province,
                }
                for unit in (board.units_by_province.values() if board else [])
            ],
            "scOwners": (board.sc_owners.copy() if board else {}),
            "theaters": compute_theater_metrics(
                board.units_by_province if board else {},
                board.sc_owners if board else {},
            ),
        }

        return payload

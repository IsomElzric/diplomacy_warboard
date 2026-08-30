class DashboardPayloadBuilder:
    """
    Builds a front-end-ready payload for the selected season and all country histories.
    """

    @staticmethod
    def build(game_timeline, year, season):
        summary = game_timeline.get_season_summary(year, season)
        payload = {
            "selectedSeason": {"year": year, "season": season},
            "countries": {},
        }

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

        return payload

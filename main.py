from IO.OrderParser import OrderParser
from Engines.FinalPositionEngine import FinalPositionEngine
from Engines.SCOwnershipEngine import SCOwnershipEngine
from Engines.MetricsEngine import MetricsEngine
from Engines.ForecastEngine import ForecastEngine
from States.CountryState import CountryState
from States.GameState import GameState
from States.GameTimeline import GameTimeline
from IO.ConsoleOutput import ConsoleOutput
from Data.location_data import compute_country_geography_from_units
from Data.supply_centers import reset_supply_centers


def load_text(path):
    with open(path, "r") as f:
        return f.read()


def build_starting_baseline_timeline(year=1901, season="Spring"):
    reset_supply_centers()
    ownership = SCOwnershipEngine().compute({}, season=season)
    country_states = build_country_states(ownership, {}, year=year, season=season)

    metrics = MetricsEngine()
    metrics.compute_metrics(country_states)

    timeline = GameTimeline(year, season)
    for state in country_states:
        timeline.add_country_state(state.country, state)

    return timeline


def build_country_states(ownership, final_positions, year, season):
    states = []
    ownership_by_province = {
        province: owner
        for owner, provinces in ownership.items()
        if owner not in {"", "Neutral"}
        for province in provinces
    }
    unit_positions_by_country = {}
    for province, owner in final_positions.items():
        if owner and owner != "Neutral":
            unit_positions_by_country.setdefault(owner, set()).add(province)

    for country, scs in ownership.items():
        if not country or country == "Neutral":
            continue

        sc_count = len(scs)
        unit_count = sum(1 for p, c in final_positions.items() if c == country)
        if unit_count == 0:
            unit_count = sc_count

        cs = CountryState(
            country=country,
            year=year,
            season=season,
            sc=sc_count,
            units=unit_count,
            builds=0,
        )

        hostile_countries = {
            other_country for other_country in ownership
            if other_country not in {"Neutral", country}
        }
        geography = compute_country_geography_from_units(
            country,
            unit_positions_by_country.get(country, set()),
            ownership_by_province,
            hostile_countries,
        )
        cs.active_fronts = geography["active_fronts"]
        cs.isolation = geography["isolation"]
        cs.encirclement = geography["encirclement"]

        states.append(cs)

    return states


def build_game_timeline(season_data):
    """
    season_data: list of (year, season, text_block)
    Example: [(1901, 'Spring', 'Austria\n...'), (1901, 'Fall', 'Austria\n...')]
    """
    reset_supply_centers()
    timeline = GameTimeline()
    previous_country_units = {}

    for year, season, text in season_data:
        parser = OrderParser()
        movement_orders, retreat_orders = parser.parse(text)

        final_positions = FinalPositionEngine().compute_final_positions(
            movement_orders,
            retreat_orders,
        )

        ownership = SCOwnershipEngine().compute(final_positions, season=season)
        country_states = build_country_states(
            ownership,
            final_positions,
            year=year,
            season=season,
        )

        country_position_counts = {}
        for country_name in {state.country for state in country_states}:
            country_position_counts[country_name] = sum(
                1 for province, owner in final_positions.items() if owner == country_name
            )

        for state in country_states:
            country_name = state.country
            current_units = country_position_counts.get(country_name, state.units)

            if season.lower() == "winter":
                build_count = sum(
                    1 for order in movement_orders.get(country_name, [])
                    if order.get("action") == "BUILD" and order.get("success")
                )
                disband_count = sum(
                    1 for order in movement_orders.get(country_name, [])
                    if order.get("action") == "DISBAND" and order.get("success")
                )

                baseline_units = previous_country_units.get(country_name, current_units)
                state.units = current_units if current_units is not None else max(0, baseline_units + build_count - disband_count)
                state.builds = build_count
                previous_country_units[country_name] = state.units
            else:
                state.units = current_units
                state.builds = 0
                previous_country_units[country_name] = state.units

        timeline.add_season_states(year, season, country_states)

    metrics = MetricsEngine()
    for country, country_timeline in timeline.country_timelines.items():
        history = [snapshot.country_state for snapshot in country_timeline.snapshots]
        if history:
            metrics.compute_metrics_by_country(history)

    return timeline


def main():
    text = load_text("1901s.txt")

    parser = OrderParser()
    movement_orders, retreat_orders = parser.parse(text)

    final_positions = FinalPositionEngine().compute_final_positions(
        movement_orders,
        retreat_orders,
    )

    ownership = SCOwnershipEngine().compute(final_positions, season="Spring")

    country_states = build_country_states(
        ownership,
        final_positions,
        year=1901,
        season="Spring",
    )

    metrics = MetricsEngine()
    metrics.compute_metrics(country_states)

    game = GameState(1901, "Spring")
    for cs in country_states:
        game.add_country_state(cs)

    game_timeline = GameTimeline(1901, "Spring")
    for cs in country_states:
        game_timeline.add_country_state(cs.country, cs)

    forecast = ForecastEngine().forecast(game)
    ConsoleOutput().display(forecast, "Spring 1901")

    england_timeline = game_timeline.get_country_timeline("England")
    if england_timeline:
        england_snapshot = england_timeline.get_snapshot(1901, "Spring")
        if england_snapshot:
            print(
                f"England timeline snapshot: SC={england_snapshot.country_state.sc}, "
                f"Momentum={england_snapshot.country_state.momentum}, "
                f"Active Fronts={england_snapshot.country_state.active_fronts}"
            )


if __name__ == "__main__":
    main()

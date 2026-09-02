from IO.OrderParser import OrderParser
from Engines.FinalPositionEngine import FinalPositionEngine
from Engines.SCOwnershipEngine import SCOwnershipEngine
from Engines.MetricsEngine import MetricsEngine
from Engines.ForecastEngine import ForecastEngine
from States.CountryState import CountryState
from States.GameState import GameState
from States.GameTimeline import GameTimeline
from IO.ConsoleOutput import ConsoleOutput
from Data.location_data import PROVINCE_DATA, compute_country_geography_from_units
from Data.supply_centers import STARTING_SUPPLY_CENTERS, reset_supply_centers
from States.UnitState import UnitState
from States.BoardState import BoardState
from Engines.FrontMetricsEngine import FrontMetricsEngine


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
    season_data: list[(year, season, text_block)]
    Fully board-aware refactor.
    """

    reset_supply_centers()
    timeline = GameTimeline()
    metrics_engine = MetricsEngine()
    front_engine = FrontMetricsEngine()

    previous_board = None
    previous_country_states = {}

    for year, season, text in season_data:

        # --- 1. Parse orders ---
        parser = OrderParser()
        movement_orders, retreat_orders = parser.parse(text)

        # --- 2. Adjudicate final positions ---
        final_positions = FinalPositionEngine().compute_final_positions(
            movement_orders,
            retreat_orders,
        )

        # --- 3. Build new BoardState ---
        if season.lower() == "winter" and previous_board is not None:
            board = previous_board.copy(year=year, season=season)
        else:
            board = BoardState(year, season)
            if previous_board is not None:
                board.sc_owners = previous_board.sc_owners.copy()

        # SC ownership (Fall only)
        ownership = SCOwnershipEngine().compute(final_positions, season)
        sc_owners = {}
        for owner, provinces in ownership.items():
            for prov in provinces:
                sc_owners[prov] = owner
        if season.lower() == "winter":
            board.sc_owners = previous_board.sc_owners.copy() if previous_board is not None else sc_owners
        else:
            board.sc_owners = sc_owners

        # Units: one per occupied province, with order attached
        if season.lower() != "winter":
            retreat_sources = {
                order["from"]
                for country_orders in retreat_orders.values()
                for order in country_orders
            }
            for country, orders in movement_orders.items():
                for o in orders:
                    if o["from"] in retreat_sources:
                        continue
                    prov = o["to"] if o.get("success") and o.get("to") else o["from"]
                    if prov and final_positions.get(prov) == country:
                        board.add_unit(UnitState(
                            country=country,
                            unit_type=o["unit"],
                            province=prov,
                            order=o
                        ))
            for country, orders in retreat_orders.items():
                for o in orders:
                    if o.get("success") and o.get("to") and final_positions.get(o["to"]) == country:
                        board.add_unit(UnitState(
                            country=country,
                            unit_type=o["unit"],
                            province=o["to"],
                            order=o,
                        ))
        else:
            for country, orders in movement_orders.items():
                for o in orders:
                    if o.get("action") == "BUILD" and o.get("success"):
                        province = o.get("from")
                        if province:
                            board.add_unit(UnitState(
                                country=country,
                                unit_type=o["unit"],
                                province=province,
                                order=o,
                            ))
                    elif o.get("action") == "DISBAND" and o.get("success"):
                        province = o.get("from")
                        if province:
                            board.remove_unit(province)

        # --- 4. Build CountryState objects from board ---
        country_states = []
        board_countries = set(previous_country_states)
        previous_sc_owners = (
            previous_board.sc_owners if previous_board is not None else STARTING_SUPPLY_CENTERS
        )
        unit_country_by_source = {
            order["from"]: country
            for country, country_orders in movement_orders.items()
            for order in country_orders
            if order.get("from")
        }

        for owner in sc_owners.values():
            if owner not in ("", "Neutral"):
                board_countries.add(owner)
        for country, orders in movement_orders.items():
            if country:
                board_countries.add(country)
        for province, owner in final_positions.items():
            if owner and owner not in ("", "Neutral"):
                board_countries.add(owner)

        for country in sorted(board_countries):
            owned_scs = board.get_owned_scs_for_country(country)
            units = board.get_units_for_country(country)

            cs = CountryState(
                country=country,
                year=year,
                season=season,
                sc=len(owned_scs),
                units=len(units),
                builds=0,
            )

            # Holds & supports from orders
            orders = movement_orders.get(country, [])
            cs.order_count = len(orders)
            cs.successful_orders = sum(1 for order in orders if order.get("success"))
            cs.holds = sum(1 for o in orders if o.get("action") == "HOLD")
            cs.supports = sum(1 for o in orders if o.get("action") == "SUPPORT")
            cs.moves = sum(1 for o in orders if o.get("action") == "MOVE")
            cs.support_holds = sum(
                1 for o in orders
                if o.get("action") == "SUPPORT" and " - " not in (o.get("to") or "")
            )
            cs.support_attacks = sum(
                1 for o in orders
                if o.get("action") == "SUPPORT" and " - " in (o.get("to") or "")
            )
            cs.detailed_order_outcomes = True
            cs.successful_defensive_orders = sum(
                1 for o in orders
                if o.get("success") and (
                    o.get("action") == "HOLD"
                    or (o.get("action") == "SUPPORT" and " - " not in (o.get("to") or ""))
                )
            )
            cs.successful_offensive_orders = sum(
                1 for o in orders
                if o.get("success") and (
                    o.get("action") == "MOVE"
                    or (o.get("action") == "SUPPORT" and " - " in (o.get("to") or ""))
                )
            )
            center_moves = [
                order for order in orders
                if order.get("action") == "MOVE"
                and order.get("to") in STARTING_SUPPLY_CENTERS
                and previous_sc_owners.get(order["to"], "") != country
            ]
            cs.center_targets = len(center_moves)
            cs.successful_center_attacks = sum(1 for order in center_moves if order.get("success"))
            cs.allied_supports = sum(
                1 for order in orders
                if order.get("action") == "SUPPORT"
                and unit_country_by_source.get((order.get("to") or "").split()[0]) not in (None, country)
            )
            threatened_centers = {
                order.get("to")
                for enemy_country, enemy_orders in movement_orders.items()
                if enemy_country != country
                for order in enemy_orders
                if order.get("action") == "MOVE"
                and order.get("to") in owned_scs
            }
            cs.threatened_centers = len(threatened_centers)
            defended_centers = {
                order.get("from") for order in orders
                if order.get("action") == "HOLD" and order.get("from") in threatened_centers
            }
            defended_centers.update(
                (order.get("to") or "").split()[0]
                for order in orders
                if order.get("action") == "SUPPORT"
                and " - " not in (order.get("to") or "")
                and (order.get("to") or "").split()[0] in threatened_centers
            )
            cs.defended_threatened_centers = len(defended_centers)
            front_unit_counts = {}
            for unit in units:
                front_id = PROVINCE_DATA.get(unit.province, {}).get("front_id")
                if front_id:
                    front_unit_counts[front_id] = front_unit_counts.get(front_id, 0) + 1
            cs.front_concentration = (
                max(front_unit_counts.values()) / len(units)
                if front_unit_counts and units else 0.0
            )

            # Geography metrics
            hostile = [c for c in sc_owners.values() if c not in ("", "Neutral", country)]
            geo = front_engine.compute(country, owned_scs, hostile)
            cs.active_fronts = geo["active_fronts"]
            cs.isolation = geo["isolation"]
            cs.encirclement = geo["encirclement"]

            country_states.append(cs)

        # --- 5. Winter build/disband logic ---
        if season.lower() == "winter":
            for cs in country_states:
                country_name = cs.country
                orders = movement_orders.get(country_name, [])

                build_count = sum(
                    1 for o in orders
                    if o.get("action") == "BUILD" and o.get("success")
                )
                disband_count = sum(
                    1 for o in orders
                    if o.get("action") == "DISBAND" and o.get("success")
                )

                prev_state = previous_country_states.get(country_name)
                base_units = prev_state.units if prev_state else len(board.get_units_for_country(country_name))
                cs.units = max(0, base_units + build_count - disband_count)
                cs.builds = build_count

        # --- 6. Add to timeline ---
        timeline.add_season_states(year, season, country_states)
        timeline.board_states[(year, season)] = board

        # --- 7. Derive normalized board features and historical metrics ---
        histories = {
            country_name: [snapshot.country_state for snapshot in country_timeline.snapshots]
            for country_name, country_timeline in timeline.country_timelines.items()
        }
        metrics_engine.compute_metrics_by_country(histories)

        # Update continuity
        previous_board = board
        previous_country_states = {cs.country: cs for cs in country_states}

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

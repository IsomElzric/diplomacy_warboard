import unittest

from Data.location_data import (
    PROVINCE_DATA,
    compute_country_geography_metrics,
    get_legal_neighbors_for_unit,
    get_fronts_for_country,
)
from Engines.MonteCarloEngine import MonteCarloEngine, SimulationState, SimulatedUnit
from States.CountryState import CountryState
from States.GameState import GameState
from States.TimelineState import CountryTimeline, SeasonSnapshot
from main import build_country_states


class CountryTimelineAndMonteCarloTests(unittest.TestCase):
    def test_province_metadata_contains_location_and_front_data(self):
        self.assertIn("Par", PROVINCE_DATA)
        self.assertIn("front_id", PROVINCE_DATA["Par"])
        self.assertIn("neighbors", PROVINCE_DATA["Par"])

    def test_country_timeline_tracks_snapshots_and_front_count(self):
        timeline = CountryTimeline("England")
        timeline.add_snapshot(SeasonSnapshot(1901, "Spring", CountryState("England", sc=3, units=3)))
        timeline.add_snapshot(SeasonSnapshot(1902, "Spring", CountryState("England", sc=4, units=4)))

        self.assertEqual(timeline.country, "England")
        self.assertEqual(len(timeline.snapshots), 2)
        self.assertEqual(timeline.front_count(), 0)

    def test_country_timeline_tracks_season_metric_history(self):
        timeline = CountryTimeline("England")

        first = CountryState("England", sc=3, units=3)
        first.momentum = 1
        first.ema_momentum = 0.5
        first.cgi = 0.2
        first.active_fronts = 1
        first.isolation = 0.4
        first.encirclement = 0.1

        second = CountryState("England", sc=4, units=4)
        second.momentum = 2
        second.ema_momentum = 1.0
        second.cgi = 0.5
        second.active_fronts = 2
        second.isolation = 0.2
        second.encirclement = 0.2

        timeline.add_snapshot(SeasonSnapshot(1901, "Spring", first))
        timeline.add_snapshot(SeasonSnapshot(1902, "Spring", second))

        self.assertEqual(timeline.metric_history("momentum"), [1, 2])
        self.assertEqual(timeline.metric_history("active_fronts"), [1, 2])
        self.assertEqual(timeline.get_snapshot(1902, "Spring").country_state.sc, 4)

    def test_owning_multiple_fronts_counts_as_multiple_active_fronts(self):
        fronts = get_fronts_for_country("England", {"Lon", "Edi", "Lvp", "Yor"})
        self.assertEqual(len(fronts), 2)
        self.assertIn("NorthSea", fronts)
        self.assertIn("EnglishChannel", fronts)

    def test_geography_metrics_compute_isolation_and_encirclement(self):
        metrics = compute_country_geography_metrics(
            "England",
            {"Lon", "Edi", "Lvp"},
            {"Fra", "Ger", "Rus", "Tur"},
        )

        self.assertGreaterEqual(metrics["active_fronts"], 1)
        self.assertGreaterEqual(metrics["isolation"], 0)
        self.assertGreaterEqual(metrics["encirclement"], 0)

    def test_build_country_states_assigns_geography_metrics(self):
        ownership = {
            "England": {"Lon", "Edi", "Lvp"},
            "France": {"Par", "Mar", "Bre"},
            "Neutral": set(),
        }

        states = build_country_states(ownership, {}, year=1901, season="Spring")
        england = next(state for state in states if state.country == "England")

        self.assertGreaterEqual(england.active_fronts, 1)
        self.assertGreaterEqual(england.isolation, 0)
        self.assertGreaterEqual(england.encirclement, 0)

    def test_monte_carlo_engine_returns_country_probabilities(self):
        game = GameState(1901, "Spring")
        england = CountryState("England", sc=3, units=3)
        england.momentum = 2
        england.ema_momentum = 1
        england.cgi = 0.5
        england.active_fronts = 2
        england.isolation = 0.2
        england.encirclement = 0.1
        game.add_country_state(england)

        forecast = MonteCarloEngine().simulate(game, iterations=25)
        self.assertIn("England", forecast)
        self.assertGreaterEqual(forecast["England"], 0)
        self.assertLessEqual(forecast["England"], 1)

    def test_monte_carlo_uses_strategic_state_not_just_sc(self):
        game = GameState(1901, "Spring")

        england = CountryState("England", sc=7, units=7)
        england.momentum = 4
        england.ema_momentum = 2.5
        england.cgi = 2.1
        england.active_fronts = 4
        england.holds = 6
        england.supports = 5
        england.isolation = 0.2
        england.encirclement = 0.3
        england.growth_rate = 1.1
        england.unit_growth = 2
        england.build_effeciency = 0.5
        game.add_country_state(england)

        france = CountryState("France", sc=3, units=3)
        france.momentum = 0.5
        france.ema_momentum = 0.2
        france.cgi = 0.2
        france.active_fronts = 1
        france.holds = 1
        france.supports = 1
        france.isolation = 1.2
        france.encirclement = 1.0
        france.growth_rate = 0.1
        france.unit_growth = 0
        france.build_effeciency = 0.1
        game.add_country_state(france)

        forecast = MonteCarloEngine().simulate(game, iterations=2000)
        self.assertGreater(forecast["England"], forecast["France"])

    def test_simulation_state_copies_board_without_mutating_live_game(self):
        game = GameState(1902, "Fall")
        game.board.add_unit(SimulatedUnit("England", "F", "NTH"))
        game.board.sc_owners["Lon"] = "England"

        simulation = MonteCarloEngine(seed=7).create_simulation_state(game)
        copied = simulation.copy()
        copied.units_by_province.pop("NTH")
        copied.sc_owners["Lon"] = "France"

        self.assertIn("NTH", simulation.units_by_province)
        self.assertEqual(simulation.sc_owners["Lon"], "England")
        self.assertIn("NTH", game.board.units_by_province)
        self.assertEqual(game.board.sc_owners["Lon"], "England")

    def test_legal_neighbors_respect_army_and_fleet_movement(self):
        self.assertIn("Wal", get_legal_neighbors_for_unit("Lon", "A"))
        self.assertNotIn("ENG", get_legal_neighbors_for_unit("Lon", "A"))
        self.assertIn("ENG", get_legal_neighbors_for_unit("Lon", "F"))
        self.assertNotIn("Yor", get_legal_neighbors_for_unit("Lon", "F"))

    def test_aggressive_policy_values_enemy_supply_center_more_than_defensive_policy(self):
        simulation = SimulationState(
            1902,
            "Fall",
            {"Pic": SimulatedUnit("France", "A", "Pic")},
            {"Bel": "England"},
        )
        unit = simulation.units_by_province["Pic"]
        aggressive = CountryState("France")
        aggressive.posture = "Aggressive"
        defensive = CountryState("France")
        defensive.posture = "Defensive"

        aggressive_bel = next(candidate for candidate in MonteCarloEngine(seed=1).generate_unit_candidates(simulation, aggressive, unit) if candidate.get("to") == "Bel")
        defensive_bel = next(candidate for candidate in MonteCarloEngine(seed=1).generate_unit_candidates(simulation, defensive, unit) if candidate.get("to") == "Bel")

        self.assertGreater(aggressive_bel["weight"], defensive_bel["weight"])

    def test_resolver_bounces_equal_strength_moves(self):
        simulation = SimulationState(
            1902,
            "Spring",
            {
                "Lon": SimulatedUnit("England", "A", "Lon"),
                "Lvp": SimulatedUnit("France", "A", "Lvp"),
            },
            {},
        )

        result = MonteCarloEngine().resolve_movement(simulation, [
            {"action": "MOVE", "from": "Lon", "to": "Wal"},
            {"action": "MOVE", "from": "Lvp", "to": "Wal"},
        ])

        self.assertSetEqual(result.successful_moves, set())
        self.assertSetEqual(result.bounced_moves, {"Lon", "Lvp"})
        self.assertIn("Lon", result.state.units_by_province)
        self.assertIn("Lvp", result.state.units_by_province)

    def test_resolver_uses_support_to_dislodge_holding_enemy(self):
        simulation = SimulationState(
            1902,
            "Spring",
            {
                "Bur": SimulatedUnit("France", "A", "Bur"),
                "Pic": SimulatedUnit("France", "A", "Pic"),
                "Bel": SimulatedUnit("England", "A", "Bel"),
            },
            {},
        )

        result = MonteCarloEngine().resolve_movement(simulation, [
            {"action": "MOVE", "from": "Bur", "to": "Bel"},
            {"action": "SUPPORT", "from": "Pic", "support_from": "Bur", "support_to": "Bel"},
        ])

        self.assertSetEqual(result.successful_moves, {"Bur"})
        self.assertEqual(result.state.units_by_province["Bel"].country, "France")
        self.assertEqual(result.dislodged_units["Bel"].country, "England")

    def test_retreat_resolver_preserves_dislodged_unit_in_legal_province(self):
        simulation = SimulationState(
            1902,
            "Spring",
            {
                "Bur": SimulatedUnit("France", "A", "Bur"),
                "Pic": SimulatedUnit("France", "A", "Pic"),
                "Bel": SimulatedUnit("England", "A", "Bel"),
            },
            {"Hol": "England"},
        )
        engine = MonteCarloEngine(seed=1)
        movement = engine.resolve_movement(simulation, [
            {"action": "MOVE", "from": "Bur", "to": "Bel"},
            {"action": "SUPPORT", "from": "Pic", "support_from": "Bur", "support_to": "Bel"},
        ])
        england = CountryState("England")
        england.posture = "Defensive"

        retreat = engine.resolve_retreats(movement, {"England": england, "France": CountryState("France")})

        self.assertEqual(retreat.successful_retreats, {"Bel": "Hol"})
        self.assertEqual(retreat.state.units_by_province["Hol"].country, "England")
        self.assertEqual(retreat.state.units_by_province["Bel"].country, "France")

    def test_turn_generator_converts_hold_into_support_for_friendly_attack(self):
        simulation = SimulationState(
            1902,
            "Spring",
            {
                "Bur": SimulatedUnit("France", "A", "Bur"),
                "Pic": SimulatedUnit("France", "A", "Pic"),
            },
            {"Bel": "England"},
        )
        engine = MonteCarloEngine(seed=1)
        engine.choose_unit_intent = lambda state, country, unit: (
            {"action": "MOVE", "from": "Bur", "to": "Bel", "weight": 1.0}
            if unit.province == "Bur"
            else {"action": "HOLD", "from": "Pic", "weight": 0.05}
        )
        engine.random.uniform = lambda start, end: end

        intents = engine.generate_turn_intents(simulation, {"France": CountryState("France")})
        support = next(intent for intent in intents if intent["from"] == "Pic")

        self.assertEqual(support["action"], "SUPPORT")
        self.assertEqual(support["support_from"], "Bur")
        self.assertEqual(support["support_to"], "Bel")

    def test_resolver_cuts_support_when_enemy_attacks_supporter(self):
        simulation = SimulationState(
            1902,
            "Spring",
            {
                "Yor": SimulatedUnit("England", "A", "Yor"),
                "Lon": SimulatedUnit("England", "A", "Lon"),
                "Wal": SimulatedUnit("France", "A", "Wal"),
                "ENG": SimulatedUnit("France", "F", "ENG"),
            },
            {},
        )

        result = MonteCarloEngine().resolve_movement(simulation, [
            {"action": "MOVE", "from": "Yor", "to": "Wal"},
            {"action": "SUPPORT", "from": "Lon", "support_from": "Yor", "support_to": "Wal"},
            {"action": "MOVE", "from": "ENG", "to": "Lon"},
        ])

        self.assertIn("Lon", result.cut_supports)
        self.assertSetEqual(result.successful_moves, set())
        self.assertSetEqual(result.bounced_moves, {"Yor", "ENG"})

    def test_winter_resolver_builds_in_vacant_controlled_home_centers(self):
        simulation = SimulationState(
            1902,
            "Fall",
            {"Gas": SimulatedUnit("France", "A", "Gas")},
            {"Par": "France", "Mar": "France", "Bre": "France"},
        )

        result = MonteCarloEngine().resolve_winter(simulation, [
            {"action": "BUILD", "country": "France", "province": "Bre", "unit_type": "F"},
            {"action": "BUILD", "country": "France", "province": "Par", "unit_type": "A"},
        ])

        self.assertEqual(result.state.season, "Winter")
        self.assertEqual(result.state.units_by_province["Bre"].unit_type, "F")
        self.assertEqual(result.state.units_by_province["Par"].unit_type, "A")
        self.assertEqual(len(result.builds), 2)
        self.assertEqual(result.unfilled_builds, {})
        self.assertNotIn("Bre", simulation.units_by_province)

    def test_winter_resolver_honors_explicit_removal(self):
        simulation = SimulationState(
            1902,
            "Fall",
            {
                "Lon": SimulatedUnit("England", "A", "Lon"),
                "Yor": SimulatedUnit("England", "A", "Yor"),
            },
            {"Lon": "England"},
        )

        result = MonteCarloEngine().resolve_winter(simulation, [
            {"action": "DISBAND", "country": "England", "province": "Yor"},
        ])

        self.assertNotIn("Yor", result.state.units_by_province)
        self.assertIn("Lon", result.state.units_by_province)
        self.assertEqual(result.removals, [{"country": "England", "unit_type": "A", "province": "Yor"}])
        self.assertEqual(result.unfilled_removals, {})

    def test_simulation_trial_captures_supply_centers_in_fall(self):
        game = GameState(1902, "Spring")
        game.add_country_state(CountryState("France"))
        game.board.add_unit(SimulatedUnit("France", "A", "Pic"))
        game.board.sc_owners["Bel"] = ""
        engine = MonteCarloEngine(seed=1)

        engine.generate_turn_intents = lambda state, countries: [
            {"action": "MOVE", "from": "Pic", "to": "Bel"}
            if "Pic" in state.units_by_province
            else {"action": "HOLD", "from": "Bel"}
        ]
        result = engine.simulate_trial(game, horizon_years=1, stalemate_seasons=4)

        self.assertEqual(result.state.sc_owners["Bel"], "France")
        self.assertEqual(result.terminal_reason, "horizon")

    def test_simulation_trial_stops_after_repeated_operational_stalemate(self):
        game = GameState(1902, "Spring")
        game.add_country_state(CountryState("England"))
        game.board.add_unit(SimulatedUnit("England", "A", "Lon"))
        game.board.sc_owners.update({"Lon": "England", "Edi": "England", "Lvp": "England"})
        engine = MonteCarloEngine(seed=1)
        engine.generate_turn_intents = lambda state, countries: [
            {"action": "HOLD", "from": province}
            for province in state.units_by_province
        ]

        result = engine.simulate_trial(game, horizon_years=3, stalemate_seasons=2)

        self.assertEqual(result.terminal_reason, "stalemate")
        self.assertIsNone(result.winner)
        self.assertEqual(result.movement_seasons, 2)
        self.assertEqual(result.stagnant_seasons, 2)

    def test_simulation_trial_stops_when_country_reaches_solo_threshold(self):
        game = GameState(1902, "Fall")
        game.add_country_state(CountryState("France"))
        game.board.add_unit(SimulatedUnit("France", "A", "Par"))
        game.board.sc_owners = {f"SC{index}": "France" for index in range(18)}
        engine = MonteCarloEngine(seed=1)
        engine.generate_turn_intents = lambda state, countries: [
            {"action": "HOLD", "from": province}
            for province in state.units_by_province
        ]

        result = engine.simulate_trial(game, horizon_years=3)

        self.assertEqual(result.terminal_reason, "solo")
        self.assertEqual(result.winner, "France")
        self.assertEqual(result.movement_seasons, 1)

    def test_aggregate_trials_report_draws_and_expected_material(self):
        game = GameState(1902, "Spring")
        game.add_country_state(CountryState("England"))
        game.board.add_unit(SimulatedUnit("England", "A", "Lon"))
        game.board.sc_owners.update({"Lon": "England", "Edi": "England", "Lvp": "England"})
        engine = MonteCarloEngine(seed=1)
        engine.generate_turn_intents = lambda state, countries: [
            {"action": "HOLD", "from": province}
            for province in state.units_by_province
        ]

        forecast = engine.simulate_trials(game, iterations=4, horizon_years=3, stalemate_seasons=2)

        self.assertEqual(forecast["draw_probability"], 1.0)
        self.assertEqual(forecast["terminal_reasons"]["stalemate"], 4)
        self.assertEqual(forecast["countries"]["England"]["win_probability"], 0.0)
        self.assertEqual(forecast["countries"]["England"]["expected_scs"], 3.0)
        self.assertEqual(forecast["countries"]["England"]["expected_units"], 3.0)
        self.assertEqual(forecast["countries"]["England"]["expected_rank"], 1.0)
        self.assertEqual(forecast["countries"]["England"]["elimination_probability"], 0.0)
        self.assertEqual(forecast["countries"]["England"]["home_center_loss_probability"], 0.0)


if __name__ == "__main__":
    unittest.main()

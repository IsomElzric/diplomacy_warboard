import unittest

from Data.location_data import (
    PROVINCE_DATA,
    compute_country_geography_metrics,
    get_fronts_for_country,
)
from Engines.MonteCarloEngine import MonteCarloEngine
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


if __name__ == "__main__":
    unittest.main()

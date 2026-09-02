import unittest

from States.CountryState import CountryState
from States.GameTimeline import GameTimeline


class GameTimelineTests(unittest.TestCase):
    def test_game_timeline_tracks_country_sequences(self):
        game_timeline = GameTimeline(1901, "Spring")

        england_1 = CountryState("England", year=1901, season="Spring", sc=3, units=3)
        england_1.momentum = 1
        england_1.active_fronts = 1

        england_2 = CountryState("England", year=1902, season="Spring", sc=4, units=4)
        england_2.momentum = 2
        england_2.active_fronts = 2

        game_timeline.add_country_state("England", england_1)
        game_timeline.add_country_state("England", england_2)

        timeline = game_timeline.get_country_timeline("England")
        self.assertIsNotNone(timeline)
        self.assertEqual(len(timeline.snapshots), 2)
        self.assertEqual(timeline.metric_history("momentum"), [1, 2])
        self.assertEqual(game_timeline.get_snapshot("England", 1902, "Spring").country_state.sc, 4)

    def test_game_timeline_summary_for_specific_season(self):
        game_timeline = GameTimeline(1901, "Spring")

        england = CountryState("England", year=1901, season="Spring", sc=3, units=3)
        france = CountryState("France", year=1901, season="Spring", sc=3, units=3)

        game_timeline.add_country_state("England", england)
        game_timeline.add_country_state("France", france)

        summary = game_timeline.get_season_summary(1901, "Spring")
        self.assertIn("England", summary)
        self.assertIn("France", summary)

    def test_game_timeline_records_full_season_batch(self):
        game_timeline = GameTimeline()

        england = CountryState("England", year=1901, season="Spring", sc=3, units=3)
        france = CountryState("France", year=1901, season="Spring", sc=3, units=3)

        game_timeline.add_season_states(1901, "Spring", [england, france])

        self.assertIn("England", game_timeline.get_season_summary(1901, "Spring"))
        self.assertEqual(len(game_timeline.get_country_timeline("England").snapshots), 1)

    def test_build_game_timeline_from_multiple_seasons(self):
        from main import build_game_timeline

        season_data = [
            (1901, "Spring", "Austria\nA Vie H  SUCCEEDS\n\nEngland\nF Lon H  SUCCEEDS\n"),
            (1901, "Fall", "Austria\nA Vie H  SUCCEEDS\n\nEngland\nF Lon H  SUCCEEDS\n"),
        ]

        timeline = build_game_timeline(season_data)
        self.assertIn("England", timeline.get_season_summary(1901, "Spring"))
        self.assertIn("England", timeline.get_season_summary(1901, "Fall"))


if __name__ == "__main__":
    unittest.main()

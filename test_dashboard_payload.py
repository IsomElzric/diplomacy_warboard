import unittest

from States.CountryState import CountryState
from States.DashboardPayload import DashboardPayloadBuilder
from States.GameTimeline import GameTimeline


class DashboardPayloadTests(unittest.TestCase):
    def test_dashboard_payload_includes_current_and_history(self):
        game_timeline = GameTimeline(1901, "Spring")

        england = CountryState("England", year=1901, season="Spring", sc=3, units=3)
        england.momentum = 1
        england.active_fronts = 2

        next_england = CountryState("England", year=1902, season="Spring", sc=4, units=4)
        next_england.momentum = 2
        next_england.active_fronts = 3

        game_timeline.add_country_state("England", england)
        game_timeline.add_country_state("England", next_england)

        payload = DashboardPayloadBuilder.build(game_timeline, 1901, "Spring")

        self.assertIn("England", payload["countries"])
        self.assertEqual(payload["selectedSeason"]["year"], 1901)
        self.assertEqual(payload["selectedSeason"]["season"], "Spring")
        self.assertEqual(payload["countries"]["England"]["current"]["sc"], 3)
        self.assertEqual(len(payload["countries"]["England"]["history"]), 2)


if __name__ == "__main__":
    unittest.main()

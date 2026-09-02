import unittest

from States.CountryState import CountryState
from States.BoardState import BoardState
from States.DashboardPayload import DashboardPayloadBuilder
from States.GameTimeline import GameTimeline
from States.UnitState import UnitState


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

    def test_board_backed_payload_includes_detailed_simulation_forecast(self):
        game_timeline = GameTimeline(1901, "Spring")
        england = CountryState("England", year=1901, season="Spring", sc=1, units=1)
        game_timeline.add_country_state("England", england)
        board = BoardState(1901, "Spring")
        board.add_unit(UnitState("England", "A", "Lon"))
        board.sc_owners["Lon"] = "England"
        game_timeline.add_board_state(1901, "Spring", board)

        payload = DashboardPayloadBuilder.build(game_timeline, 1901, "Spring")

        self.assertIn("forecastDetails", payload)
        self.assertIn("England", payload["forecastDetails"]["countries"])
        self.assertIn("expected_scs", payload["forecastDetails"]["countries"]["England"])
        self.assertIn("draw_probability", payload["forecastDetails"])
        self.assertEqual(len(payload["board"]["theaters"]), 4)
        self.assertIn("North Atlantic", [theater["name"] for theater in payload["board"]["theaters"]])


if __name__ == "__main__":
    unittest.main()

import unittest

from Engines.MetricsEngine import MetricsEngine
from IO.OrderParser import OrderParser
from States.CountryState import CountryState


class CountryBlockParsingAndMetricsTests(unittest.TestCase):
    def test_parser_keeps_orders_grouped_by_country(self):
        text = """
Austria
A Bud - Tri  SUCCEEDS
A Vie - Tyr  SUCCEEDS

England
F Edi - NTH  SUCCEEDS
A Lvp - Yor  SUCCEEDS

France
A Mar - Spa  SUCCEEDS
A Par - Bur  SUCCEEDS
"""

        movement, retreats = OrderParser().parse(text)

        self.assertEqual(set(movement.keys()), {"Austria", "England", "France"})
        self.assertEqual(len(movement["Austria"]), 2)
        self.assertEqual(len(movement["England"]), 2)
        self.assertEqual(len(movement["France"]), 2)

    def test_metrics_group_by_country_not_across_country_blocks(self):
        states = [
            CountryState("England", sc=3, units=3),
            CountryState("France", sc=2, units=2),
        ]

        MetricsEngine().compute_metrics_by_country(states)

        self.assertEqual(states[0].momentum, 0)
        self.assertEqual(states[1].momentum, 0)
        self.assertEqual(states[0].ema_momentum, 0)
        self.assertEqual(states[1].ema_momentum, 0)

    def test_metrics_are_calculated_across_a_country_history(self):
        spring = CountryState("England", year=1901, season="Spring", sc=3, units=3)
        fall = CountryState("England", year=1901, season="Fall", sc=4, units=4)

        MetricsEngine().compute_metrics_by_country([spring, fall])

        self.assertGreater(fall.momentum, 0)
        self.assertGreater(fall.ema_momentum, 0)
        self.assertGreater(fall.cgi, 0)

    def test_metrics_derive_operational_and_position_features_from_board_inputs(self):
        spring = CountryState("England", year=1901, season="Spring", sc=3, units=3)
        fall = CountryState("England", year=1901, season="Fall", sc=4, units=3)
        fall.order_count = 4
        fall.successful_orders = 3
        fall.holds = 1
        fall.supports = 1

        MetricsEngine().compute_metrics_by_country([spring, fall])

        self.assertEqual(fall.order_success_rate, 0.75)
        self.assertEqual(fall.unit_sc_ratio, 0.75)
        self.assertGreater(fall.board_control, 0)
        self.assertGreater(fall.operational_efficiency, 0)
        self.assertGreater(fall.strategic_position, 0)

    def test_unit_efficiency_separates_successful_defense_from_aggression(self):
        defense = CountryState("England", year=1901, season="Fall", sc=3, units=3)
        defense.order_count = 3
        defense.successful_orders = 3
        defense.holds = 2
        defense.support_holds = 1

        offense = CountryState("France", year=1901, season="Fall", sc=3, units=3)
        offense.order_count = 3
        offense.successful_orders = 3
        offense.moves = 2
        offense.support_attacks = 1

        MetricsEngine().compute_metrics_by_country([defense, offense])

        self.assertEqual(defense.unit_efficiency, 1.0)
        self.assertEqual(defense.posture, "Defensive")
        self.assertEqual(offense.unit_efficiency, 1.0)
        self.assertEqual(offense.posture, "Aggressive")

    def test_predictive_rates_capture_conversion_threat_coverage_and_allied_support(self):
        state = CountryState("England", year=1901, season="Fall", sc=4, units=4)
        state.center_targets = 2
        state.successful_center_attacks = 1
        state.threatened_centers = 2
        state.defended_threatened_centers = 1
        state.supports = 2
        state.allied_supports = 1
        state.front_concentration = 0.75

        MetricsEngine().compute_metrics_by_country([state])

        self.assertEqual(state.center_conversion_rate, 0.5)
        self.assertEqual(state.threat_coverage_rate, 0.5)
        self.assertEqual(state.allied_support_rate, 0.5)
        self.assertEqual(state.front_concentration, 0.75)


if __name__ == "__main__":
    unittest.main()

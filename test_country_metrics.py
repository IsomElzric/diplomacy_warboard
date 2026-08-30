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


if __name__ == "__main__":
    unittest.main()

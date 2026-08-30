import unittest

from Data.supply_centers import reset_supply_centers
from Engines.SCOwnershipEngine import SCOwnershipEngine
from main import build_country_states


class StartingUnitBaselineTests(unittest.TestCase):
    def test_country_states_start_with_supply_center_units_when_no_units_are_recorded(self):
        ownership = {
            "England": ["Lon", "Lvp", "Edi"],
            "France": ["Par", "Bre", "Mar"],
            "Germany": ["Ber", "Kie", "Mun"],
            "Italy": ["Ven", "Rom", "Nap"],
            "Austria": ["Vie", "Bud", "Tri"],
            "Russia": ["War", "Mos", "Stp"],
            "Turkey": ["Con", "Smy", "Ank"],
        }

        states = build_country_states(
            ownership,
            {},
            year=1901,
            season="Spring",
        )

        state_by_country = {state.country: state for state in states}

        self.assertEqual(state_by_country["Germany"].units, 3)
        self.assertEqual(state_by_country["Italy"].units, 3)
        self.assertEqual(state_by_country["England"].units, 3)

    def test_supply_center_reset_keeps_germany_and_italy_in_game(self):
        reset_supply_centers()
        ownership = SCOwnershipEngine().compute({}, season="Spring")

        self.assertIn("Germany", ownership)
        self.assertIn("Italy", ownership)
        self.assertEqual(len(ownership["Germany"]), 3)
        self.assertEqual(len(ownership["Italy"]), 3)

    def test_fall_ownership_updates_for_neutral_provinces_without_keyerror(self):
        reset_supply_centers()
        final_positions = {"Bel": "England"}

        ownership = SCOwnershipEngine().compute(final_positions, season="Fall")

        self.assertIn("England", ownership)
        self.assertIn("Bel", ownership["England"])
        self.assertNotIn("Bel", ownership["Neutral"])


if __name__ == "__main__":
    unittest.main()

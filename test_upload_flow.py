import unittest

from dashboard_server import (
    build_dashboard_payload,
    build_uploaded_payload,
    merge_uploaded_game_text,
    parse_uploaded_game_text,
    reset_active_game_timeline,
)


class UploadFlowTests(unittest.TestCase):
    def test_single_season_upload_uses_selected_season_metadata(self):
        text = """
England
F Edi - NTH  SUCCEEDS
A Lvp - Yor  SUCCEEDS
France
A Par - Bur  SUCCEEDS
"""

        payload = build_uploaded_payload(text, year=1902, season="Fall", mode="season")

        self.assertEqual(payload["selectedSeason"]["year"], 1902)
        self.assertEqual(payload["selectedSeason"]["season"], "Fall")
        self.assertIn("England", payload["countries"])
        self.assertIn("France", payload["countries"])

    def test_full_game_upload_parses_multiple_season_blocks(self):
        text = """
Spring 1901
England
F Edi - NTH  SUCCEEDS
A Lvp - Yor  SUCCEEDS

Fall 1901
England
F Edi - NTH  SUCCEEDS
A Lvp - Yor  SUCCEEDS
"""

        blocks = parse_uploaded_game_text(text)

        self.assertEqual(len(blocks), 2)
        self.assertEqual(blocks[0][0], 1901)
        self.assertEqual(blocks[0][1], "Spring")
        self.assertEqual(blocks[1][0], 1901)
        self.assertEqual(blocks[1][1], "Fall")

    def test_markdown_bold_markers_are_stripped_from_input(self):
        text = """
**Austria**
F ADR S Tyr - Ven  SUCCEEDS

**England**
F ENG - MAO  SUCCEEDS
"""

        payload = build_uploaded_payload(text, year=1901, season="Spring", mode="season")

        self.assertIn("Austria", payload["countries"])
        self.assertIn("England", payload["countries"])

    def test_merge_uploaded_game_text_keeps_previous_seasons_and_replaces_duplicate_season_entries(self):
        existing = """
Spring 1901
England
F Edi - NTH  SUCCEEDS

Fall 1901
England
F Edi - NTH  SUCCEEDS
"""
        new = """
Winter 1901
England
F Edi - NTH  SUCCEEDS
"""

        merged = merge_uploaded_game_text(existing, new, year=1901, season="Winter")

        self.assertIn("Spring 1901", merged)
        self.assertIn("Fall 1901", merged)
        self.assertIn("Winter 1901", merged)

        duplicate_existing = """
Spring 1901
England
A Lvp - Yor  SUCCEEDS
"""
        duplicate_merged = merge_uploaded_game_text(
            duplicate_existing,
            """
Spring 1901
England
F Edi - NTH  SUCCEEDS
""",
            year=1901,
            season="Spring",
        )

        self.assertIn("F Edi - NTH  SUCCEEDS", duplicate_merged)
        self.assertNotIn("A Lvp - Yor  SUCCEEDS", duplicate_merged)

    def test_historical_season_lookup_returns_saved_game_data(self):
        text = """
Spring 1901
England
F Edi - NTH  SUCCEEDS
A Lvp - Yor  SUCCEEDS

Fall 1901
England
F Edi - NTH  SUCCEEDS
A Lvp - Yor  SUCCEEDS
"""

        build_uploaded_payload(text, mode="full")
        payload = build_dashboard_payload(year=1901, season="Spring")

        self.assertEqual(payload["selectedSeason"]["year"], 1901)
        self.assertEqual(payload["selectedSeason"]["season"], "Spring")
        self.assertIn("England", payload["countries"])
        self.assertGreater(len(payload["countries"]["England"]["history"]), 0)

    def test_reset_active_game_timeline_removes_saved_server_game(self):
        build_uploaded_payload("""
Spring 1901
England
F Edi - NTH  SUCCEEDS
""", mode="full")

        reset_active_game_timeline()

        self.assertIsNone(build_dashboard_payload()["selectedSeason"])

    def test_winter_build_and_disband_orders_are_parsed(self):
        text = """
Austria
A Nap Disband  SUCCEEDS

England
F NTH Disband  SUCCEEDS

France
F Bre Build  SUCCEEDS
A Par Build  SUCCEEDS

Russia
A Mos Build  SUCCEEDS
"""

        from IO.OrderParser import OrderParser
        movement, retreats = OrderParser().parse(text)

        self.assertEqual(movement["Austria"][0]["action"], "DISBAND")
        self.assertEqual(movement["France"][1]["action"], "BUILD")
        self.assertEqual(movement["Russia"][0]["action"], "BUILD")

    def test_full_game_keeps_country_unit_totals_across_winter_builds(self):
        from main import build_game_timeline

        timeline = build_game_timeline([
            (1901, "Fall", """
France
A Par - Bur  SUCCEEDS
A Mar - Spa  SUCCEEDS
F Bre - MAO  SUCCEEDS
"""),
            (1901, "Winter", """
France
A Par Build  SUCCEEDS
A Mar Build  SUCCEEDS
F Bre Build  SUCCEEDS
"""),
        ])

        france_state = timeline.get_season_summary(1901, "Winter")["France"]
        self.assertEqual(france_state.units, 6)

    def test_winter_uses_current_season_positions_instead_of_stale_previous_total(self):
        from main import build_game_timeline

        timeline = build_game_timeline([
            (1901, "Fall", """
France
A Par - Bur  SUCCEEDS
A Mar H  SUCCEEDS
F Bre H  SUCCEEDS
"""),
            (1901, "Winter", """
France
A Mar Disband  SUCCEEDS
A Par Disband  SUCCEEDS
"""),
        ])

        france_state = timeline.get_season_summary(1901, "Winter")["France"]
        self.assertEqual(france_state.units, 1)


if __name__ == "__main__":
    unittest.main()

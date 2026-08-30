import unittest

from dashboard_server import build_uploaded_payload, parse_uploaded_game_text


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


if __name__ == "__main__":
    unittest.main()

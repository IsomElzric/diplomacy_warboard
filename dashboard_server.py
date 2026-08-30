import json
import mimetypes
import os
import re
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
from urllib.parse import parse_qs, urlparse

from main import build_game_timeline, build_starting_baseline_timeline
from Data.supply_centers import reset_supply_centers
from States.DashboardPayload import DashboardPayloadBuilder

ROOT = Path(__file__).resolve().parent
FRONTEND_DIR = ROOT / "frontend"


def normalize_order_text(text):
    if not text:
        return ""

    cleaned_lines = []
    for line in text.splitlines():
        sanitized = line.strip().replace("**", "").strip()
        if sanitized:
            cleaned_lines.append(sanitized)

    return "\n".join(cleaned_lines)


def parse_uploaded_game_text(text):
    if not text or not text.strip():
        return []

    text = normalize_order_text(text)
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    blocks = []
    current_year = None
    current_season = None
    current_block = []

    def flush_block():
        nonlocal current_year, current_season, current_block
        if current_year is not None and current_season is not None and current_block:
            blocks.append((current_year, current_season, "\n".join(current_block)))
        current_year = None
        current_season = None
        current_block = []

    season_header = re.compile(r"^(Spring|Summer|Fall|Winter)\s+(\d{4})$", re.IGNORECASE)
    season_header_alt = re.compile(r"^(\d{4})\s+(Spring|Summer|Fall|Winter)$", re.IGNORECASE)

    for line in lines:
        match = season_header.match(line)
        if match:
            flush_block()
            current_year = int(match.group(2))
            current_season = match.group(1).title()
            continue

        match = season_header_alt.match(line)
        if match:
            flush_block()
            current_year = int(match.group(1))
            current_season = match.group(2).title()
            continue

        if current_year is not None and current_season is not None:
            current_block.append(line)
        else:
            current_block.append(line)

    flush_block()
    return blocks


def build_uploaded_payload(text, year=1901, season="Spring", mode="season"):
    if not text or not text.strip():
        raise ValueError("Order text is required.")

    reset_supply_centers()
    cleaned_text = normalize_order_text(text)

    if mode == "full":
        blocks = parse_uploaded_game_text(cleaned_text)
        if not blocks:
            raise ValueError("No valid season blocks were found in the uploaded game text.")
        selected_year, selected_season = blocks[-1][0], blocks[-1][1]
        game_timeline = build_game_timeline(blocks)
        return DashboardPayloadBuilder.build(game_timeline, selected_year, selected_season)

    season_year = int(year) if year is not None else 1901
    season_name = season or "Spring"
    game_timeline = build_game_timeline([(season_year, season_name, cleaned_text)])
    return DashboardPayloadBuilder.build(game_timeline, season_year, season_name)


def build_dashboard_payload(year=1901, season="Spring"):
    reset_supply_centers()
    return {"selectedSeason": None, "countries": {}}


class DashboardHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, directory=str(FRONTEND_DIR), **kwargs):
        super().__init__(*args, directory=directory, **kwargs)

    def _serve_frontend_asset(self, relative_path):
        candidate = (FRONTEND_DIR / relative_path.lstrip("/")).resolve()
        if not str(candidate).startswith(str(FRONTEND_DIR.resolve())):
            self.send_error(403, "Forbidden")
            return
        if not candidate.is_file():
            self.send_error(404, "Not Found")
            return

        content = candidate.read_bytes()
        mime_type, _ = mimetypes.guess_type(str(candidate))
        self.send_response(200)
        self.send_header("Content-Type", mime_type or "application/octet-stream")
        self.send_header("Content-Length", str(len(content)))
        self.end_headers()
        self.wfile.write(content)

    def do_GET(self):
        parsed = urlparse(self.path)

        if parsed.path == "/api/dashboard":
            query = parse_qs(parsed.query)
            year = int(query.get("year", ["1901"])[0])
            season = query.get("season", ["Spring"])[0]
            payload = build_dashboard_payload(year=year, season=season)

            body = json.dumps(payload).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return

        if parsed.path in ("/", "/index.html"):
            self._serve_frontend_asset("index.html")
            return

        if parsed.path in ("/app.js", "/styles.css"):
            self._serve_frontend_asset(parsed.path.lstrip("/"))
            return

        return super().do_GET()

    def do_POST(self):
        parsed = urlparse(self.path)

        if parsed.path == "/api/upload":
            content_length = int(self.headers.get("Content-Length", "0"))
            raw = self.rfile.read(content_length) if content_length > 0 else b"{}"

            try:
                data = json.loads(raw.decode("utf-8")) if raw else {}
            except json.JSONDecodeError:
                data = {}

            text = (data.get("text") or "").strip()
            year = data.get("year")
            season = data.get("season")
            mode = (data.get("mode") or "season").lower()

            try:
                payload = build_uploaded_payload(text=text, year=year, season=season, mode=mode)
            except ValueError as exc:
                body = json.dumps({"error": str(exc)}).encode("utf-8")
                self.send_response(400)
                self.send_header("Content-Type", "application/json")
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                self.wfile.write(body)
                return

            body = json.dumps(payload).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return

        self.send_response(404)
        self.end_headers()


if __name__ == "__main__":
    HOST = os.environ.get("HOST", "0.0.0.0")
    PORT = int(os.environ.get("PORT", "8000"))
    server = ThreadingHTTPServer((HOST, PORT), DashboardHandler)
    print(f"Serving Diplomacy dashboard at http://{HOST}:{PORT}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server")
    finally:
        server.server_close()

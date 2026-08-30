# Diplomacy Warboard

A Python-based Diplomacy command center for tracking countries, real-time supply-center state, seasonal order parsing, and tactical metrics across a game timeline.

This project is designed to help you:
- upload Diplomacy order text by season or full game
- initialize country baselines from starting supply centers and units
- parse movement and winter build/disband orders
- calculate country-level metrics over time
- render a tactical dashboard with a warboard, history, and focus views

## Project structure

- `main.py` — core timeline and baseline logic
- `dashboard_server.py` — local HTTP server for the web dashboard and upload API
- `Data/` — supply-center and province metadata
- `Engines/` — ownership, metrics, forecast, and final-position logic
- `IO/` — order parsing and input handling
- `States/` — country and game state models
- `frontend/` — HTML, CSS, and JavaScript for the command-center UI
- `test_*.py` — regression tests covering parsing, metrics, timeline behavior, and upload flow

## Core workflow

1. Load order text for a season or a full game.
2. Parse the text into country blocks and unit actions.
3. Compute final positions and supply-center ownership.
4. Build country states and metrics for each season.
5. Render the dashboard with a selected country, timeline, and warboard summary.

## Gameplay assumptions

- The game begins from the standard seven-player Diplomacy setup.
- Each country starts with its home supply centers and one unit per home center unless the uploaded data provides a different state.
- Neutral provinces are excluded from ownership and are not treated as controlled by any country.
- The game timeline is built from season snapshots and keeps country histories for trend analysis.

## Local development

From the project root:

```bash
python dashboard_server.py
```

Then open:

```text
http://127.0.0.1:8000/
```

## How the dashboard works

The app is designed like a tactical command center for a Diplomacy game.

- The left panel lets you pick a season and a country focus.
- The warboard shows provinces by controlling power.
- The comparison table summarizes supply centers, unit counts, and momentum.
- The focus panel highlights the selected country’s status, forecast outlook, and recent history.
- Uploading order text updates the in-memory game state and recalculates the timeline.

## Uploading orders

The web app supports:
- single season uploads
- full-game uploads
- winter build/disband parsing

Example payload flow:
- choose the season and mode in the upload panel
- paste standard Diplomacy adjudication text
- click Load Orders

A typical season block looks like this:

```text
England
F Edi - NTH SUCCEEDS
A Lvp - Yor SUCCEEDS

France
F Bre - MAO SUCCEEDS
A Par - Bur SUCCEEDS

Germany
A Ber - Kie FAILS
F Kie - Bal SUCCEEDS

Winter 1901
England
F NTH Build SUCCEEDS
```

This project expects country names as headers, followed by unit action lines that reflect movement, holds, and winter actions.

## Testing

Run the suite with:

```bash
python -m unittest discover -p "test*.py"
```

## Deployment

This project is compatible with a simple Python web deployment such as Render.

Use the app entry point:

```bash
python dashboard_server.py
```

The server listens on the environment-provided `PORT`, and binds to `0.0.0.0` when deployed.

## Notes

This is a tactical analysis dashboard for Diplomacy, not a full game engine adjudicator. It focuses on:
- order parse reliability
- timeline generation
- nation metrics and momentum
- visual command-center output

## License

This project is intended for personal and study use in a Diplomacy analysis workflow.

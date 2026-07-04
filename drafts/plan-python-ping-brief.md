Python ping module E2E validation. Small code change + unit tests. No network.

Task 1: Create `sandbox_ping.py` at the repo root with a function `ping() -> str` that returns exactly `"pong"`.

Task 2: Create `tests/test_ping.py` with a `unittest.TestCase` that imports `sandbox_ping` and asserts `ping() == "pong"`. Do not add other test files.

Exactly 2 tasks. Each task Write path is a single `.py` file. At most 2 requirement checkboxes per task. Verification uses `python3 -c` or `python3 -m unittest` only — no pytest, no pip install, no network calls.

Suggested verify (orchestrator may refine in task bodies):
- T001: `python3 -c "import sandbox_ping; assert sandbox_ping.ping() == 'pong'"`
- T002: `PYTHONPATH=. python3 -m unittest tests.test_ping -v`

Note: code write paths classify as standard tier (not simple/docs-only); plan approval allows standard tasks.

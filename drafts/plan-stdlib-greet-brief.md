Stdlib greet package E2E validation. Three-task progressive build on top of existing sandbox_ping.py. No network.

Task 1: Create `src/sandbox_greet/greet.py` with function `greet(name: str) -> str` that returns exactly `f"Hello, {name}"` (e.g. `greet("World")` → `"Hello, World"`). No other modules in this task.

Task 2: Create `src/sandbox_greet/__init__.py` that re-exports `greet` so `from sandbox_greet import greet` works when `PYTHONPATH=src`.

Task 3: Create `tests/test_greet.py` with a `unittest.TestCase` that imports `greet` from `sandbox_greet` and asserts `greet("World") == "Hello, World"`. Do not add other test files.

Exactly 3 tasks. Each task Write path is a single `.py` file. At most 2 requirement checkboxes per task. Verification uses `python3 -c`, `test -f`, or `python3 -m unittest` only — no pytest, no pip install, no network calls.

Suggested verify (orchestrator may refine in task bodies):
- T001: `test -f src/sandbox_greet/greet.py && PYTHONPATH=src python3 -c "from sandbox_greet.greet import greet; assert greet('World') == 'Hello, World'"`
- T002: `test -f src/sandbox_greet/__init__.py && PYTHONPATH=src python3 -c "from sandbox_greet import greet; assert greet('World') == 'Hello, World'"`
- T003: `PYTHONPATH=src python3 -m unittest tests.test_greet -v`

Note: code write paths classify as standard tier; plan approval allows standard tasks. Do not modify sandbox_ping.py or tests/test_ping.py.

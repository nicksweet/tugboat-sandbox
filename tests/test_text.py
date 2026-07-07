import unittest
from sandbox_text import normalize_ws

class TestNormalizeWs(unittest.TestCase):
    def test_normalize_ws_basic(self):
        self.assertEqual(normalize_ws("  foo   bar  "), "foo bar")

if __name__ == '__main__':
    unittest.main()
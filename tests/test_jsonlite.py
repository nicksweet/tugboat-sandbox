import unittest
from sandbox_jsonlite import loads


class TestJsonlite(unittest.TestCase):
    def test_loads_simple_object(self):
        self.assertEqual(loads('{"x": 1}'), {"x": 1})


if __name__ == "__main__":
    unittest.main()
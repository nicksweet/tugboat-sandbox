import unittest
from sandbox_time import format_seconds

class TestTime(unittest.TestCase):
    def test_format_seconds(self):
        self.assertEqual(format_seconds(3661), "01:01:01")

if __name__ == '__main__':
    unittest.main()
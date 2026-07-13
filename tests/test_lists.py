import unittest
from sandbox_lists import dedupe_sorted


class TestDedupeSorted(unittest.TestCase):
    def test_dedupe_sorted_basic(self):
        self.assertEqual(dedupe_sorted([2, 1, 2]), [1, 2])


if __name__ == "__main__":
    unittest.main()
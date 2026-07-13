import unittest
from sandbox_lists import dedupe_sorted


class TestDedupeSorted(unittest.TestCase):
    def test_dedupe_sorted_basic(self):
        self.assertEqual(dedupe_sorted([2, 1, 2]), [1, 2])

    def test_dedupe_sorted_empty(self):
        self.assertEqual(dedupe_sorted([]), [])

    def test_dedupe_sorted_already_unique(self):
        self.assertEqual(dedupe_sorted([1, 2, 3]), [1, 2, 3])

    def test_dedupe_sorted_all_duplicates(self):
        self.assertEqual(dedupe_sorted([5, 5, 5]), [5])


if __name__ == "__main__":
    unittest.main()
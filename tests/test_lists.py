import unittest
from sandbox_lists import dedupe_sorted

class TestDedupeSorted(unittest.TestCase):
    def test_dedupe_sorted(self):
        self.assertTrue(dedupe_sorted([2, 1, 2]) == [1, 2])

if __name__ == '__main__':
    unittest.main()
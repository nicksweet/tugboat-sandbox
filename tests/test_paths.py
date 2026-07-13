import unittest
from sandbox_paths import join_parts


class TestJoinParts(unittest.TestCase):
    def test_join_parts(self):
        self.assertEqual(join_parts("a", "b"), "a/b")


if __name__ == "__main__":
    unittest.main()
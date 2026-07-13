import unittest
from sandbox_email import normalize_email


class TestNormalizeEmail(unittest.TestCase):
    def test_normalize_email_strips_and_lowers(self):
        self.assertEqual(normalize_email("  A@B.COM "), "a@b.com")


if __name__ == "__main__":
    unittest.main()
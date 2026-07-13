"""Unit tests for sandbox_email package."""

import unittest
from sandbox_email import normalize_email


class TestNormalizeEmail(unittest.TestCase):
    """Test cases for normalize_email function."""

    def test_normalize_email_strips_whitespace_and_lowercases(self):
        """Test that normalize_email strips whitespace and lowercases the email."""
        self.assertEqual(normalize_email("  A@B.COM "), "a@b.com")


if __name__ == "__main__":
    unittest.main()
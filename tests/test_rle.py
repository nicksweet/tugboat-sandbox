"""Unit tests for sandbox_rle encode function."""

import unittest
from sandbox_rle import encode


class TestEncode(unittest.TestCase):
    """Test cases for the encode function."""

    def test_encode_aaabbc(self):
        """Test encoding of 'aaabbc' produces 'a3b2c1'."""
        self.assertEqual(encode("aaabbc"), "a3b2c1")


if __name__ == "__main__":
    unittest.main()
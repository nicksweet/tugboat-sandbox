import unittest
from sandbox_rle import encode


class TestRLEEncode(unittest.TestCase):
    def test_encode_aaabbc(self):
        self.assertEqual(encode("aaabbc"), "a3b2c1")


if __name__ == "__main__":
    unittest.main()
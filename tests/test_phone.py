import unittest
from sandbox_phone import normalize_digits


class TestNormalizeDigits(unittest.TestCase):
    def test_normalize_digits(self):
        self.assertEqual(normalize_digits('(555) 123-4567'), '5551234567')


if __name__ == '__main__':
    unittest.main()
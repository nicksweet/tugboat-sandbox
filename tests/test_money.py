import unittest
from sandbox_money import cents_to_str

class TestMoney(unittest.TestCase):
    def test_cents_to_str(self):
        self.assertEqual(cents_to_str(1234), "$12.34")

if __name__ == '__main__':
    unittest.main()
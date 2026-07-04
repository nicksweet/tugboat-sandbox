import unittest
from sandbox_calc import add, sub, mean

class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_sub(self):
        self.assertEqual(sub(5, 2), 3)

    def test_mean(self):
        self.assertEqual(mean([1.0, 2.0, 3.0]), 2.0)

    def test_mean_empty(self):
        with self.assertRaises(ValueError):
            mean([])

if __name__ == '__main__':
    unittest.main()
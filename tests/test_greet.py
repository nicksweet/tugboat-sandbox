import unittest
from sandbox_greet import greet

class TestGreet(unittest.TestCase):
    def test_greet_world(self):
        self.assertEqual(greet("World"), "Hello, World")
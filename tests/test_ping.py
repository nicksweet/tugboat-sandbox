import unittest
import sandbox_ping

class TestPing(unittest.TestCase):
    def test_ping(self):
        self.assertEqual(sandbox_ping.ping(), "pong")
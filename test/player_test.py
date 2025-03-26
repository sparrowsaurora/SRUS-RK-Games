import unittest
from app.player import Player

class TestPlayer(unittest.TestCase):
    def test_uid(self):
        # Tests if .uid() returns Unique ID correctly
        player = Player("1", "John Doe")
        self.assertEqual(player.uid(), "1")

    def test_name(self):
        # Tests if .name() returns player name correctly
        player = Player("1", "Jane Doe")
        self.assertEqual(player.name(), "Jane Doe")

unittest.main()
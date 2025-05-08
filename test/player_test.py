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

    def test_score(self):
        player = Player("1", "John Doe", 1)
        self.assertEqual(player.score, 1)

    def test_comparison(self):
        player = Player("1", "John Doe", 1)
        player2 = Player("2", "Jane Doe")
        self.assertEqual(player.score, 1)
        self.assertEqual(player2.score, 0)
        self.assertFalse(player.score == player2.score)
        self.assertTrue(player.score > player2.score)
        self.assertFalse(player.score < player2.score)
        self.assertNotEqual(player.score, player2.score)
        player3 = Player("3", "example", 1)
        self.assertEqual(player.score, player3.score)

unittest.main()
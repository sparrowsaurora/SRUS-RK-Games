import unittest

from app.player_hashmap import PlayerHashMap
from app.player import Player

class TestPlayerHashMap(unittest.TestCase):
    def setUp(self):
        self.hm = PlayerHashMap()
        self.player1 = Player("1", "John Doe")
        self.player2 = Player("2", "Jane Doe")
        self.player3 = Player("3", "unknown")
        self.player4 = Player("4", "Another")
        self.player5 = Player("5", "Another One")
        self.player6 = Player("6", "More Players")
        self.player7 = Player("7", "Even More")

    def test_insert_and_retrieve_single_player(self):
        self.hm[self.player1] = self.player1
        self.assertTrue(self.hm.__contains__(self.player1))
        self.assertEqual(self.hm[self.player1], self.player1)

    def test_insert_multiple_players_same_list(self):
        # Force players into same list by monkey patching get_index
        index = self.hm.get_index(self.player1)
        self.hm.get_index = lambda x: index

        self.hm[self.player1] = self.player1
        self.hm[self.player2] = self.player2
        self.hm[self.player3] = self.player3

        self.assertEqual(len(self.hm.hashmap[index]), 3)
        self.assertTrue(self.hm.__contains__(self.player1))
        self.assertTrue(self.hm.__contains__(self.player2))
        self.assertTrue(self.hm.__contains__(self.player3))


    def test_insert_players_multiple_lists(self):
        self.hm[self.player1] = self.player1
        self.hm[self.player2] = self.player2
        self.hm[self.player4] = self.player4
        self.hm[self.player5] = self.player5
        self.hm[self.player6] = self.player6
        self.hm[self.player7] = self.player7

        total = len(self.hm)
        self.assertEqual(total, 6)

        # Make sure all players are in the hashmap
        for player in [self.player1, self.player2, self.player4, self.player5, self.player6, self.player7]:
            self.assertTrue(self.hm.__contains__(player))
            self.assertEqual(self.hm[player], player)

    def test_delete_player(self):
        self.hm[self.player1] = self.player1
        self.hm[self.player2] = self.player2
        del self.hm[self.player1]

        self.assertFalse(self.hm.__contains__(self.player1))
        self.assertTrue(self.hm.__contains__(self.player2))


        with self.assertRaises(KeyError):
            _ = self.hm[self.player1]

    def test_get_nonexistent_player_raises(self):
        with self.assertRaises(KeyError):
            _ = self.hm["nonexistent"]

    def test_contains(self):
        self.hm[self.player3] = self.player3
        self.assertTrue(self.player3 in self.hm)
        self.assertFalse(self.player1 in self.hm)

    def test_len_and_repr(self):
        self.assertEqual(len(self.hm), 0)
        self.hm[self.player1] = self.player1
        self.hm[self.player2] = self.player2
        self.assertEqual(len(self.hm), 2)
        self.assertIn("PlayerHashMap", repr(self.hm))

if __name__ == "__main__":
    unittest.main()

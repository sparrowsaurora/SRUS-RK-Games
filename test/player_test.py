import unittest
from player import Player

class TestPlayer(unittest.TestCase):
    # def test_uid(self):
    #     # Tests if .uid() returns Unique ID correctly
    #     player = Player("1", "John Doe")
    #     self.assertEqual(player.uid(), "1")

    # def test_name(self):
    #     # Tests if .name() returns player name correctly
    #     player = Player("1", "Jane Doe")
    #     self.assertEqual(player.name(), "Jane Doe")

    # def test_score(self):
    #     player = Player("1", "John Doe", 1)
    #     self.assertEqual(player.score, 1)

    # def test_comparison(self):
    #     player = Player("1", "John Doe", 1)
    #     player2 = Player("2", "Jane Doe")
    #     self.assertEqual(player.score, 1)
    #     self.assertEqual(player2.score, 0)
    #     self.assertFalse(player.score == player2.score)
    #     self.assertTrue(player.score > player2.score)
    #     self.assertFalse(player.score < player2.score)
    #     self.assertNotEqual(player.score, player2.score)
    #     player3 = Player("3", "example", 1)
    #     self.assertEqual(player.score, player3.score)

    # def test_sort(self):
    #     player_scores = [2, 6, 8, 2, 0, 3, 5, 7, 1, 4, 9]
    #     descending_scores = Player.sort_players(player_scores)
    #     ascending_scores = Player.sort_players(player_scores, True)
    #     self.assertEqual(descending_scores, [9, 8, 7, 6, 5, 4, 3, 2, 2, 1, 0])
    #     self.assertEqual(ascending_scores, [0, 1, 2, 2, 3, 4, 5, 6, 7, 8, 9])
    #     self.assertEqual(Player.sort_players([0, 0, 40, 2]), [40, 2, 0, 0])

    # def test_sort_players(self):
    #     players = [Player(player_name="Alice", unique_id='01', score=10), 
    #                Player(player_name="Bob", unique_id='02', score=5), 
    #                Player(player_name="Charlie", unique_id='03', score=15)]
    #     # note: ensure initialization code is valid for **your** implementation

    #     # do **not** change the following code:
    #     sorted_players = sorted(players)

    #     # players must be sorted by score as shown here:
    #     manually_sorted_players = [Player(player_name="Bob", unique_id='02', score=5), 
    #                                Player(player_name="Alice", unique_id='01', score=10), 
    #                                Player(player_name="Charlie", unique_id='03', score=15)]

    #     self.assertListEqual(sorted_players, manually_sorted_players)


    # def test_players_can_be_compared_by_score(self):
    #     # note: ensure initialization code is valid for **your** implementation
    #     alice = Player(player_name="Alice", unique_id='01', score=10)
    #     bob = Player(player_name="Bob", unique_id='02', score=5)

    #     # Add the appropriate expression to the following assert test
    #     self.assertTrue(alice > bob)

    def test_player_quicksort(self):
        players = [Player(player_name="Alice", unique_id='01', score=10), 
            Player(player_name="Bob", unique_id='02', score=5), 
            Player(player_name="Charlie", unique_id='03', score=15)]
        sorted_players = Player.quicksort(players)
        print(str(sorted_players))
        solution = [
            Player(player_name="Charlie", unique_id='03', score=15), 
            Player(player_name="Alice", unique_id='01', score=10), 
            Player(player_name="Bob", unique_id='02', score=5)
            ]
        self.assertTrue(str(sorted_players) == str(solution))

unittest.main()
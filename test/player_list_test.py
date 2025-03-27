import unittest
from app.player_node import PlayerNode
from app.player_list import PlayerList
from app.player import Player


class TestPlayerList(unittest.TestCase):
    def setUp(self):
        #Runs before each test to set up a fresh PlayerList.
        self.player_list = PlayerList()

    def test_insert_first_player(self):
        player1 = Player("1", "John Doe")
        self.player_list.insert_player(player1)

        head_node = self.player_list.get_head()

        self.assertEqual(head_node.get_player(), player1)  # Check correct player
        self.assertIsNone(head_node.get_next())  # No next node
        self.assertIsNone(head_node.get_prev())  # No prev node

    def test_insert_multiple_players(self):
        player1 = Player("1", "John Doe")
        player2 = Player("2", "Jane Doe")

        self.player_list.insert_player(player1)
        self.player_list.insert_player(player2)  # John should be the new head

        head_node = self.player_list.get_head()

        self.assertEqual(head_node.get_player(), player2)  # Head should contain John
        self.assertEqual(head_node.get_next().get_player(), player1)  # Next node is Jane
        self.assertIsNone(head_node.get_prev())  # Head has no previous node
        self.assertEqual(head_node.get_next().get_prev(), head_node)  # Jane's prev points to John


if __name__ == "__main__":
    unittest.main()

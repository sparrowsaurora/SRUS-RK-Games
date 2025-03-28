import unittest
from app.player_node import PlayerNode
from app.player_list import PlayerList
from app.player import Player

class TestPlayerList(unittest.TestCase):
    def setUp(self):
        """Set up a fresh PlayerList before each test"""
        self.player_list = PlayerList()

    def test_insert_first_player(self):
        # Test inserting the first player into an empty list
        player1 = Player("1", "John Doe")
        self.player_list.insert_player(player1)

        head_node = self.player_list.get_head
        tail_node = self.player_list.get_tail

        self.assertEqual(head_node, tail_node)  # Only one node, head == tail
        self.assertIsInstance(head_node, PlayerNode)
        self.assertEqual(head_node.get_player(), player1)
        self.assertIsNone(head_node.get_next())
        self.assertIsNone(head_node.get_prev())

    def test_insert_multiple_players(self):
        # Test inserting multiple players and list ordering
        player1 = Player("1", "John Doe")
        player2 = Player("2", "Jane Doe")

        self.player_list.insert_player(player1)  # John
        self.player_list.insert_player(player2)  # Jane inserted at head

        head_node = self.player_list.get_head
        tail_node = self.player_list.get_tail

        self.assertIsInstance(head_node, PlayerNode)
        self.assertEqual(head_node.get_player(), player2)  # Jane should be at head
        self.assertEqual(head_node.get_next().get_player(), player1)  # John next
        self.assertEqual(tail_node.get_player(), player1)  # John should be the tail
        self.assertIsNone(tail_node.get_next())  # Tail should have no next
        self.assertEqual(tail_node.get_prev(), head_node)  # John's prev is Jane

if __name__ == "__main__":
    unittest.main()

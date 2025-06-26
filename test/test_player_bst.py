import unittest
from app.player_bst import PlayerBST
from app.player_bnode import PlayerBNode
from app.player import Player

class TestPlayerBST(unittest.TestCase):
    def setUp(self):
        self.tree = PlayerBST()

    def test_insert_single_player_as_root(self):
        player1 = Player("John Doe", "1")
        self.tree.insert(player1)

        root_node = self.tree.root
        self.assertIsInstance(root_node, PlayerBNode)
        self.assertEqual(root_node.bnode_player, player1)
        self.assertIsNone(root_node.lst)
        self.assertIsNone(root_node.rst)

    def test_insert_multiple_players_correct_positioning(self):
        player1 = Player("Charlie", "1")
        player2 = Player("Alice", "2")
        player3 = Player("Eve", "3")

        self.tree.insert(player1)
        self.tree.insert(player2)
        self.tree.insert(player3)

        root = self.tree.root
        self.assertEqual(root.bnode_player.name(), "Charlie")

        self.assertIsNotNone(root.lst)
        self.assertEqual(root.lst.bnode_player.name(), "Alice")

        self.assertIsNotNone(root.rst)
        self.assertEqual(root.rst.bnode_player.name(), "Eve")

    def test_insert_duplicate_player_updates_existing(self):
        player1 = Player("Bob", "1")
        player2 = Player("Bob", "2")

        self.tree.insert(player1)
        self.tree.insert(player2)

        root = self.tree.root
        self.assertEqual(root.bnode_player.name(), "Bob")
        self.assertEqual(root.bnode_player.uid(), "2")
        self.assertEqual(root.bnode_player, player2)


import unittest
from app.player_node import PlayerNode
from app.player_list import PlayerList
from app.player import Player

class TestPlayerList(unittest.TestCase):
    def setUp(self):
        """Set up a fresh PlayerList before each test"""
        self.player_list = PlayerList()

    def test_insert_first_player_at_head(self):
        # Test inserting the first player into an empty list
        player1 = Player("1", "John Doe")
        self.player_list.insert_player_head(player1)

        head_node = self.player_list.get_head
        tail_node = self.player_list.get_tail

        self.assertEqual(head_node, tail_node)  # Only one node, head == tail
        self.assertIsInstance(head_node, PlayerNode)
        self.assertEqual(head_node.get_player(), player1)
        self.assertIsNone(head_node.get_next())
        self.assertIsNone(head_node.get_prev())

    def test_insert_multiple_players_at_head(self):
        # Test inserting multiple players and list ordering
        player1 = Player("1", "John Doe")
        player2 = Player("2", "Jane Doe")

        self.player_list.insert_player_head(player1)  # John
        self.player_list.insert_player_head(player2)  # Jane inserted at head

        head_node = self.player_list.get_head
        tail_node = self.player_list.get_tail

        self.assertIsInstance(head_node, PlayerNode) # tests if head_node is a playerNode instance
        self.assertEqual(head_node.get_player(), player2)  # Jane should be at head
        self.assertEqual(head_node.get_next().get_player(), player1)  # John next
        self.assertEqual(tail_node.get_player(), player1)  # John should be the tail
        self.assertIsNone(tail_node.get_next())  # Tail should have no next
        self.assertEqual(tail_node.get_prev(), head_node)  # John's prev is Jane

    def test_insert_multiple_players_at_tail(self):
        # test inserting multiple players at tail
        player1 = Player("1", "John Doe")
        self.player_list.insert_player_tail(player1) #insert john at tail
        player2 = Player("2", "Jane Doe")
        self.player_list.insert_player_tail(player2) # insert jane at tail

        tail_node = self.player_list.get_tail
        head_node = self.player_list.get_head

        self.assertIsInstance(tail_node, PlayerNode) # tests if tail_node is a playerNode instance
        self.assertEqual(tail_node.get_player(), player2)  # Jane should be at tail
        self.assertEqual(tail_node.get_prev().get_player(), player1)  # John next
        self.assertEqual(head_node.get_player(), player1)  # John should be the head
        self.assertIsNone(head_node.get_prev())  # Head should have no next
        self.assertEqual(head_node.get_next(), tail_node)  # John's prev is Jane

    def test_delete_tail(self):
        player1 = Player("1", "John Doe")
        self.player_list.insert_player_tail(player1)  # insert john at tail
        player2 = Player("2", "Jane Doe")
        self.player_list.insert_player_tail(player2)  # insert jane at tail
        player3 = Player("3", "unknown")
        self.player_list.insert_player_tail(player3)  # insert unknown at tail

        tail_node = self.player_list.get_tail #gets tail value
        self.assertEqual(tail_node.get_player(), player3)
        self.player_list.del_tail()
        tail_node = self.player_list.get_tail  # gets tail value
        self.assertEqual(tail_node.get_player(), player2)

    def test_delete_head(self):
        player1 = Player("1", "John Doe")
        self.player_list.insert_player_head(player1)  # insert john at head
        player2 = Player("2", "Jane Doe")
        self.player_list.insert_player_head(player2)  # insert jane at head
        player3 = Player("3", "unknown")
        self.player_list.insert_player_head(player3)  # insert unknown at head

        head_node = self.player_list.get_head  # gets head value
        self.assertEqual(head_node.get_player(), player3)
        self.player_list.del_head()
        head_node = self.player_list.get_head  # gets head value
        self.assertEqual(head_node.get_player(), player2)

    def test_delete_middle_node(self):
        player1 = Player("1", "John Doe")
        self.player_list.insert_player_head(player1)  # insert john at head
        player2 = Player("2", "Jane Doe")
        self.player_list.insert_player_head(player2)  # insert jane at head
        player3 = Player("3", "unknown")
        self.player_list.insert_player_head(player3)  # insert unknown at head

        self.player_list.del_item("2")
        self.assertEqual(self.player_list.get_head.key, "3")
        self.assertEqual(self.player_list.get_tail.key, "1")
        self.assertEqual(self.player_list.get_head.get_next().key, "1")
        self.assertEqual(self.player_list.get_tail.get_prev().key, "3")

    def test_delete_head_node(self):
        player1 = Player("1", "John Doe")
        self.player_list.insert_player_head(player1)  # insert john at head
        player2 = Player("2", "Jane Doe")
        self.player_list.insert_player_head(player2)  # insert jane at head

        self.player_list.insert_player_tail(player1)
        self.player_list.insert_player_tail(player2)

        self.player_list.del_item("1")
        self.assertEqual(self.player_list.get_head.key, "2")
        self.assertIsNone(self.player_list.get_head.get_prev())

    def test_delete_tail_node(self):
        player1 = Player("1", "John Doe")
        self.player_list.insert_player_head(player1)  # insert john at head
        player2 = Player("2", "Jane Doe")
        self.player_list.insert_player_head(player2)  # insert jane at head

        self.player_list.del_item("2")
        self.assertEqual(self.player_list.get_tail.key, "1")
        self.assertIsNone(self.player_list.get_tail.get_next())

    def test_delete_nonexistent_node(self):
        with self.assertRaises(IndexError):
            self.player_list.del_item("99")

    def test_display(self):
        player1 = Player("1", "John Doe")
        self.player_list.insert_player_head(player1)  # insert john at head
        player2 = Player("2", "Jane Doe")
        self.player_list.insert_player_head(player2)  # insert jane at head
        player3 = Player("3", "unknown")
        self.player_list.insert_player_head(player3)  # insert unknown at head

        self.player_list.display()
        self.player_list.display(False)

if __name__ == "__main__":
    unittest.main()

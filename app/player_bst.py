from app.player_bnode import PlayerBNode
from app.player import Player
class PlayerBST:
    def __init__(self):
        self.__root = None
    
    @property
    def root(self):
        return self.__root
    
    def insert(self, player):
        if self.__root is None:
            self.__root = PlayerBNode(player)
            return
        self._insert_recursive(self.__root, player)

    def _insert_recursive(self, node, player):
        if player.name() < node.bnode_player.name():
            if node.lst is None:
                node.set_lst(PlayerBNode(player))
            else:
                self._insert_recursive(node.lst, player)
        elif player.name() > node.bnode_player.name():
            if node.rst is None:
                node.set_rst(PlayerBNode(player))
            else:
                self._insert_recursive(node.rst, player)
        else:
            node.set_bnode_player(player)

    def search(self, name: str):
        return self._search_recursive(self.__root, name)

    def _search_recursive(self, node, name: str):
        if node is None:
            return None

        if name == node.bnode_player.name():
            return node.bnode_player

        if name < node.bnode_player.name():
            return self._search_recursive(node.lst, name)

        return self._search_recursive(node.rst, name)
    
    def inorder(self, node=None, players=None):
        if players is None:
            players = []
        if node is None:
            node = self.__root
            if node is None:
                return players
        if node.lst is not None:
            self.inorder(node.lst, players)
        players.append(node.bnode_player)
        if node.rst is not None:
            self.inorder(node.rst, players)
        return players



    def balance(self):
        inorder_list = self.inorder()
        sorted_players = Player.sort_players(inorder_list, ascending=True)
        self.__root = self._build_balanced_tree(sorted_players, 0, len(sorted_players) - 1)


    def _build_balanced_tree(self, players, start, end):
        if start > end:
            return None
        mid = (start + end) // 2
        node = PlayerBNode(players[mid])
        node.set_lst(self._build_balanced_tree(players, start, mid - 1))
        node.set_rst(self._build_balanced_tree(players, mid + 1, end))
        return node

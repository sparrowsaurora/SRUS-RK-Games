from app.player_bnode import PlayerBNode
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
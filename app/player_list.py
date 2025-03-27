from app.player_node import PlayerNode

class PlayerList:
    def __init__(self):
        self.__head = None

    def insert_player(self, player):
        new_node = PlayerNode(player)
        if self.__head is not None:
            new_node.set_next(self.__head)
            self.__head.set_prev(new_node)
        self.__head = new_node

    def get_head(self):
        return self.__head
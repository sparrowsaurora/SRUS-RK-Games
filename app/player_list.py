from app.player_node import PlayerNode

class PlayerList:
    def __init__(self):
        self.__head = None
        self.__tail = None

    def insert_player(self, player):
        new_node = PlayerNode(player)
        if self.__head is None:
            # If the list is empty, both head and tail should point to new_node
            self.__head = new_node
            self.__tail = new_node
        else:
            # Insert at the head, update pointers
            new_node.set_next(self.__head)
            self.__head.set_prev(new_node)
            self.__head = new_node

        if self.__head.get_next() is None:
            self.__tail = self.__head

    @property
    def get_head(self):
        return self.__head

    @property
    def get_tail(self):
        return self.__tail
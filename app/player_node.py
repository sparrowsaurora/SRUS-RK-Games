class PlayerNode:
    def __init__(self, player):
        self.__player = player
        self.__next = None
        self.__prev = None

    def get_player(self):
        return self.__player

    def get_next(self):
        return self.__next

    def get_prev(self):
        return self.__prev

    def set_next(self, next_node):
        self.__next = next_node

    def set_prev(self, prev_node):
        self.__prev = prev_node

    @property
    def key(self):
        return self.__player.uid()

    def __str__(self):
        return f"node( next: {self.__next}, Node_ID: {self.__player.uid()}, prev: {self.__prev})"
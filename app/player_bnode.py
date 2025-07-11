class PlayerBNode:
    def __init__(self, player):
        self.__player = player
        self.__lst = None
        self.__rst = None
    
    @property
    def bnode_player(self):
        return self.__player
    
    @property
    def lst(self):
        return self.__lst
    
    @property
    def rst(self):
        return self.__rst
    
    def set_rst(self, new_rst):
        self.__rst = new_rst

    def set_lst(self, new_lst):
        self.__lst = new_lst

    def set_bnode_player(self, new_player):
        self.__player = new_player

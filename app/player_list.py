from app.player_node import PlayerNode

class PlayerList:
    def __init__(self):
        self.__head = None
        self.__tail = None

    def insert_player_head(self, player):
        new_node = PlayerNode(player)
        if self.__head is None:
            # If the list is empty: head + tail point to new_node
            self.__head = new_node
            self.__tail = new_node
        else:
            # Insert head, update pointers
            new_node.set_next(self.__head)
            self.__head.set_prev(new_node)
            self.__head = new_node

        if self.__head.get_next() is None:
            self.__tail = self.__head

    def insert_player_tail(self, player):
        # insert player at tail
        new_node = PlayerNode(player)
        # again, if the list is empty:
        if self.__tail is None:
            self.__tail = new_node
            self.__head = new_node
        else:
            new_node.set_prev(self.__tail)
            self.__tail.set_next(new_node)
            self.__tail = new_node

        # if one item in list:
        if self.__tail.get_prev() is None:
            self.__head = self.__tail

    def del_tail(self):
        if self.__tail is None:
            raise IndexError("Cannot delete empty tail")
        self.__tail = self.__tail.get_prev()
        self.__tail.set_next(None)

    def del_head(self):
        if self.__head is None:
            raise IndexError("Cannot delete empty head")
        self.__head = self.__head.get_next()
        self.__head.set_prev(None)

    def del_item(self, key):
        if self.__head is None:
            raise IndexError("Cannot delete item from empty list")

        current = self.__head
        while current is not None and current.key != key:
            current = current.get_next()

        # if key was not found
        if current is None:
            raise IndexError("Item not in list")

        #if node to be deleted == head
        if current == self.__head:
            self.__head = current.get_next()
            if self.__head:
                self.__head.set_prev(None)

        # if node in middle
        if current.get_next() is not None:
            current.get_next().set_prev(current.get_prev())
        if current.get_prev() is not None:
            current.get_prev().set_next(current.get_next())

        #if node == tail
        if current == self.__tail:
            self.__tail = current.get_prev()
            if self.__tail:
                self.__tail.set_next(None)

    @property
    def get_head(self):
        return self.__head

    @property
    def get_tail(self):
        return self.__tail
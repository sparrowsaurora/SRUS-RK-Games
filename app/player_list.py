from app.player_node import PlayerNode
from app.player import Player

class PlayerList:
    def __init__(self, name: int):
        self.__head = None
        self.__tail = None
        self.name = PlayerList.find_player_list_name(name)

    @staticmethod
    def find_player_list_name(number):
        list_id = ''
        while number > 0:
            number -= 1  # Shift by 1 because A is 1 not 0
            list_id = chr(ord('A') + (number % 26)) + list_id
            number //= 26
        return list_id


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
        target_uid = key.uid() if isinstance(key, Player) else key

        while current is not None and current.key != target_uid:
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

    def get_player(self, key: str | Player):
        current = self.__head
        uuid = key.uid() if isinstance(key, Player) else key
        while current:
            if current.get_player().uid() == uuid:
                return current.get_player()
            current = current.get_next()
        raise KeyError(f"Player with UID '{uuid}' not found.")

    def contains_player(self, key: str | Player):
        try:
            self.get_player(key)
            return True
        except KeyError:
            return False

    def display(self, forward=True):
        if forward:
            # head to tail
            current = self.__head
            print(f"{self.name} -> Format: Head -> Tail")
            print("None", end=" -> ")
            while current:
                print(f"({current.get_player().uid()} | {current.get_player().name()})", end=" -> ")
                current = current.get_next()
            print("None")
        else:
            # tail to head
            current = self.__tail
            print(f"{self.name} -> Format: Tail -> Head")
            print("None", end=" -> ")
            while current:
                print(f"({current.get_player().uid()} | {current.get_player().name()})", end=" -> ")
                current = current.get_prev()
            print("None")

    def __repr__(self):
        return f"PLAYER_LIST_ID: {self.name}"

    def is_empty(self):
        return self.__head is None

    def __len__(self):
        count = 0
        current = self.__head
        while current:
            count += 1
            current = current.get_next()
        return count
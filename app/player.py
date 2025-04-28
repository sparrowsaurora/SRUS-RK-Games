class Player:
    def __init__(self, unique_id: str, player_name: str):
        self.__uid = unique_id
        self.__player_name = player_name

    def uid(self):
        return self.__uid

    def name(self):
        return self.__player_name

    def __str__(self):
        return f"Player({self.name()}, {self.uid()})"

    @classmethod
    def hash(cls, key: str) -> int:
        return sum(ord(char) for char in key)

    def __hash__(self):
        return Player.hash(self.__uid)

    def __eq__(self, other) -> bool:
        return self.uid() == other.uid()
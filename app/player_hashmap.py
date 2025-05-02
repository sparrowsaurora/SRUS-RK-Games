from app.player import Player
from app.player_list import PlayerList

class PlayerHashMap:
    SIZE: int = 10
    def __init__(self):
        self.hashmap = [PlayerList(i + 1) for i in range(self.SIZE)]

    def __repr__(self):
        total_players = sum(len(pl) for pl in self.hashmap)
        return f"PlayerHashMap(size={self.SIZE}, total_players={total_players})"

    def __len__(self):
        return sum(len(pl) for pl in self.hashmap)

    def show(self):
        print(self)
        for pl in self.hashmap:
            print(pl)

    def display(self):
        for i, pl in enumerate(self.hashmap):
            print(f"[{i}] : List[{pl.name}]", end="")
            if pl.is_empty():
                print("\nempty")
            else:
                pl.display()

    def get_index(self, key: str | Player) -> int:
        if isinstance(key, Player):
            return hash(key) % self.SIZE
        return Player.hash(key) % self.SIZE

    def __setitem__(self, key: str | Player, value: Player, at_head: bool = True) -> None:
        index = self.get_index(key)
        if at_head:
            self.hashmap[index].insert_player_head(value)
        else:
            self.hashmap[index].insert_player_tail(value)

    def __getitem__(self, key: str | Player) -> Player:
        index = self.get_index(key)
        return self.hashmap[index].get_player(key)

    def __delitem__(self, key: str | Player) -> None:
        index = self.get_index(key)
        self.hashmap[index].del_item(key)

    def __contains__(self, key: str | Player) -> bool:
        index = self.get_index(key)
        return self.hashmap[index].contains_player(key)

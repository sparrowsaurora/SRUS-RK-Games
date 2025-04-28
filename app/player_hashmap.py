from app.player import Player
from player_list import PlayerList

class PlayerHashMap:
    SIZE: int = 10
    def __init__(self):
        self.hashmap = [PlayerList(i + 1) for i in range(self.SIZE)]

    def __repr__(self):
        return f"PlayerHashMap(size={self.SIZE})"

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
        else:
            return Player.hash(key) % self.SIZE

    def __setitem__(self, key: str | Player, value: str, at_head: bool = True) -> None:
        index = self.get_index(key)
        if at_head:
            self.hashmap[index].insert_player_head(value)
        else:
            self.hashmap[index].insert_player_tail(value)


hashmap = PlayerHashMap()
hashmap.show()
hashmap.display()


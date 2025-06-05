class Player:
    def __init__(self, player_name: str, uid: str, score: int =0):
        self.__uid = uid
        self.__player_name = player_name
        self.__score = score

    def uid(self):
        return self.__uid

    def name(self):
        return self.__player_name

    def set_score(self, score: int):
        if score < 0:
            raise ValueError("Score cannot be negative")
        self.__score = score

    @property
    def score(self):
        return self.__score

    def __str__(self):
        return f"Player({self.name()}, {self.uid()}, Score = {self.__score})"

    @classmethod
    def hash(cls, key: str) -> int:
        return sum(ord(char) for char in key)

    def __hash__(self):
        return Player.hash(self.__uid)

    def __eq__(self, other) -> bool:
        return self.score == other.score

    def __ge__(self, other) -> bool:
        return self.score >= other.score

    def __gt__(self, other) -> bool:
        return self.score > other.score

    def __le__(self, other) -> bool:
        return self.score <= other.score

    def __lt__(self, other) -> bool:
        return self.score < other.score

    @staticmethod
    def sort_players(players: list, ascending: bool = False) -> list:
        """
        Utilizing Merge Sort
        :param ascending:
        :param players:
        :return: Sorted list of players
        internal functions for better readability
        """

        def merge_sort(items: list, ascending_toggle: bool) -> list:
            if len(items) <= 1:
                return items
            mid = len(items) // 2
            left = merge_sort(items[:mid], ascending_toggle)
            right = merge_sort(items[mid:], ascending_toggle)
            return merge_in(left, right, ascending_toggle)

        def merge_in(left: list, right: list, ascending_toggle: bool) -> list:
            iter_result = []
            while left and right:
                if ascending_toggle:
                    if left[0] < right[0]:
                        iter_result.append(left.pop(0))
                    else:
                        iter_result.append(right.pop(0))
                else:
                    if left[0] > right[0]:
                        iter_result.append(left.pop(0))
                    else:
                        iter_result.append(right.pop(0))
            return iter_result + left + right

        return merge_sort(players, ascending)

    @classmethod
    def quicksort(cls, players: list):
        """
        sorts players in descending order using quicksort
        for por3-inclass-5.2
        """
        def is_sorted(players: list) -> bool:
            for i in range(1, len(players)):
                if players[i] > players[i - 1]:
                    return False
            return True
        
        if len(players) <= 1 or is_sorted(players):
            return players
        pivot = players[0]
        left = []
        middle = [pivot]
        right = []
        for x in players[1:]:
            if x > pivot:
                left.append(x)
            elif x < pivot:
                right.append(x)
            else:
                middle.append(x)

        return cls.quicksort(left) + middle + cls.quicksort(right)
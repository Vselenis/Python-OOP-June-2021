from project1.player import Player


class Team:
    def __init__(self, name, rating):
        self.__name = name
        self.__rating = rating
        self.__players = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, value):
        self.__rating = value

    @property
    def players(self):
        return self.__players

    @players.setter
    def players(self, value):
        self.__players = value


    def add_player(self, player):
        if player in self.players:
            return f"Player {player.name} has already joined"
        self.players.append(player)
        return f"Player {player.name} joined team {self.name}"

    def remove_player(self, player_name):
        try:
            player = [p for p in self.players if p.name == player_name][0]
            self.players.remove(player)
            return player

        except IndexError:
            return f"Player {player_name} not found"

#
# p = Player("Pall", 1, 3, 5, 7)
#
# print("Player name:", p.name)
# print("Points sprint:", p._Player__sprint)
# print("Points dribble:", p._Player__dribble)
# print("Points passing:", p._Player__passing)
# print("Points shooting:", p._Player__shooting)
#
# print("\ncalling the __str__ method")
# print(p)
#
# print("\nAbout the team")
# t = Team("Best", 10)
# print("Team name:", t._Team__name)
# print("Teams points:", t._Team__rating)
# print("Teams players:", len(t._Team__players))
# print(t.add_player(p))
# print(t.add_player(p))
# print("Teams players:", len(t._Team__players))
# print(t.remove_player("Pall"))
# print(t.remove_player("Pall"))

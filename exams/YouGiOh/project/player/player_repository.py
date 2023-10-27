class PlayerRepository:
    def __init__(self):
        self.count = 0
        self.players = []

    def add(self, player):
        try:
            search_player = [p for p in self.players if p.username == player.username][0]
            raise ValueError(f"Player {search_player.username} already exists!")
        except IndexError:
            self.players.append(player)
            self.count += 1

    def remove(self, player):
        if player == '':
            raise ValueError("Player cannot be an empty string!")
        else:
            search_player = [p for p in self.players if p.username == player][0]
            self.players.remove(search_player)
            self.count -= 1

    def find(self, username):
        search_player = [p for p in self.players if p.username == username][0]
        return search_player

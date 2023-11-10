
class Game:
    def __init__(self):
        self.players = []

    def add_player(self, conn, address):
        if len(self.players) > 1:
            return False
        self.players.append(conn)
        return True

    def remove_player(self, conn):
        if len(self.players) == 0:
            return False
        self.players.pop(self.players.index(conn))

    def get_number_of_players(self):
        return len(self.players)

    def start(self):
        print("start game")
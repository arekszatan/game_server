import json

from ThreadClientBase import ThreadClientBase, socket_method


class GameServer(ThreadClientBase):
    def __init__(self, parent, conn, address):
        super().__init__(parent, conn, address)
        self.players = []

    def add_player(self, conn, address):
        if len(self.players) > 1:
            return False
        if conn in self.players:
            return False
        self.players.append(conn)
        return True

    def remove_player(self, conn):
        if len(self.players) == 0:
            return False
        self.players.pop(self.players.index(conn))

    def get_number_of_players(self):
        return len(self.players)

    @socket_method
    def test(self, message, prefix):
        is_added = self.add_player(self.conn, self.address)
        message = {
            "prefix": prefix,
            "data": is_added
        }

        print(self.get_number_of_players())
        self.send_data(json.dumps(message))

    @socket_method
    def test1(self, message, prefix):
        number_of_players = self.get_number_of_players()
        message = {
            "prefix": prefix,
            "data": True if number_of_players == 2 else False
        }
        print(message)
        self.send_data(json.dumps(message))

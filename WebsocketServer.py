import json

from WebsocketServerBase import WebsocketServerBase


class WebsocketServer(WebsocketServerBase):
    def __init__(self):
        super().__init__()
        self.oponent_position = 0

    # def set_players_position(self, player):
    #     self.oponent_position = player
    #     return [50, 100]

    def send_position_to_all(self, move_player):
        all_players = self.get_connected()
        for player in all_players:
            if player != move_player:
                self.oponent_position = move_player.position
        message_out = {
            "prefix": 99,
            "callback_for_all": "set_players_position",
            "data": self.oponent_position
        }
        for player in all_players:
            if player != move_player:
                player.send_data(json.dumps(message_out))



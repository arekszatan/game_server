import json
from GameRoom import GameRooms
from WebsocketServerBase import WebsocketServerBase


class WebsocketServer(WebsocketServerBase):
    def __init__(self):
        super().__init__()
        self.game_rooms = GameRooms()

    def on_thread_finished(self, game):
        game.remove_game_room()
        super(WebsocketServer, self).on_thread_finished(game)






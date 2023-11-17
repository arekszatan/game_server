import json
from ThreadClientBase import ThreadClientBase, socket_method


class GameServer(ThreadClientBase):
    def __init__(self, parent, conn, address):
        ThreadClientBase.__init__(self, parent, conn, address)
        self.position = 0

    @socket_method
    def position_after_move(self, message, prefix):
        self.position = int(message)
        message_out = {
            "prefix": prefix,
            "callback_for_all": None,
            "data": True
        }
        self.parent.send_position_to_all(self)
        self.send_data(json.dumps(message_out))





import json
from ThreadClientBase import ThreadClientBase, socket_method


class GameServer(ThreadClientBase):
    def __init__(self, parent, conn, address):
        ThreadClientBase.__init__(self, parent, conn, address)

    @socket_method
    def test(self, message, prefix):
        message_out = {
            "prefix": prefix,
            "data": self.parent.get_position()
        }

        self.send_data(json.dumps(message_out))

    @socket_method
    def test1(self, message, prefix):
        self.parent.set_position(int(message))
        message_out = {
            "prefix": prefix,
            "data": True
        }

        self.send_data(json.dumps(message_out))

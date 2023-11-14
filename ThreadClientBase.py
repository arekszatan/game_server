import threading
import logging as log
import json
from Settings import *
# from Game import Game

# game = Game()
all_socket_method = []


def socket_method(func):
    all_socket_method.append(func)


class ThreadClientBase(threading.Thread):
    def __init__(self, parent, conn, address):
        threading.Thread.__init__(self)
        self.parent = parent
        self.conn = conn
        self.address = address

    def run(self) -> None:
        while True:
            try:
                data = self.conn.recv(1024).decode()
                json_object = json.loads(data)
                prefix = json_object['prefix']
                mess_method = json_object['method']
                message = json_object['data']
                if not data:
                    self.send_data("Goodbye")
                    break
                else:
                    for method in all_socket_method:
                        if mess_method == method.__name__:
                            if method.__name__ == "ping" and not PING_LOG:
                                method(self, message, prefix)
                            else:
                                log.info(f'Get data {data} from {self.address}')
                                method(self, message, prefix)
            except Exception as e:
                log.exception(e)
                break

        log.warning("Connection Closed")
        self.conn.close()
        self.parent.on_thread_finished(self.address)

    def send_data(self, data, loging=True):
        if loging:
            log.info(f'Send data {data} to {self.address}')
        self.conn.send(data.encode())

    @socket_method
    def ping(self, message, prefix):
        message = {
            "prefix": prefix,
            "data": message
        }
        self.send_data(json.dumps(message), loging=PING_LOG)

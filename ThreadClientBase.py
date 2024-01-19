import threading
import logging as log
import json
from Settings import *
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
                data_recv = self.conn.recv(1024).decode()
                if data_recv == "":
                    break
                data_recv = data_recv.replace('}{', '},{')
                data_recv = f'[{data_recv}]'
                data_recv_json = json.loads(data_recv)
                for json_object in data_recv_json:
                    prefix = json_object['prefix']
                    mess_method = json_object['method']
                    message = json_object['data']
                    for method in all_socket_method:
                        if mess_method == method.__name__:
                            if method.__name__ == "ping" and not PING_LOG:
                                method(self, message, prefix)
                            else:
                                log.info(f'Get data {json_object} from {self.address}')
                                method(self, message, prefix)
            except Exception as e:
                log.exception(e)
                break

        log.warning("Connection Closed")
        self.conn.close()
        self.parent.on_thread_finished(self)

    def send_data(self, data, loging=True):
        if loging:
            log.info(f'Send data {data} to {self.address}')
        self.conn.send(data.encode())

    @socket_method
    def ping(self, message, prefix):
        message = {
            "prefix": prefix,
            "callback_for_all": None,
            "data": message
        }
        self.send_data(json.dumps(message), loging=PING_LOG)

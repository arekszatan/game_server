import socket
import threading
import logging as log
from Settings import *
from ThreadClient import ThreadClient


class WebsocketServer(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.running = bool
        self.connected = []
        self.server_socket = socket.socket()
        self.server_socket.bind((SERVER, PORT))
        self.server_socket.listen(ACCESSIBLE_CONNECTION)
        log.info(f'Server starting with {SERVER} and port {PORT}')

    def run(self) -> None:
        log.info(f'Server started')
        self.running = True
        conn = None
        try:
            while self.running:
                log.info(f'Waiting for new Connection...')
                conn, address = self.server_socket.accept()  # accept new connection
                log.info(f'Connected with: {address}')
                thread_client = ThreadClient(self, conn, address)
                thread_client.start()
                self.connected.append(address)
        except KeyboardInterrupt:
            if conn:
                conn.close()
            log.exception("Keyboard exception error !!!")

    def stop(self):
        log.warning(f'Server stopped')
        self.running = False

    def get_connected(self):
        return self.connected

    def on_thread_finished(self, address):
        self.connected.pop(self.connected.index(address))


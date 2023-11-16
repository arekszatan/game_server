import socket
import threading
import logging as log
from GameServer import GameServer
from Settings import *


class WebsocketServer(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.running = True
        self.connected = []
        self.server_socket = socket.socket()
        self.server_socket.bind((SERVER, PORT))
        self.server_socket.listen(ACCESSIBLE_CONNECTION)
        self.position = 0
        log.info(f'Server starting with {SERVER} and port {PORT}')

    def run(self) -> None:
        log.info(f'Server started')
        try:
            while self.running:
                log.info('Waiting for new Connection...')
                conn, address = self.server_socket.accept()
                log.info(f'Connected with: {address}')
                game = GameServer(self, conn, address)
                game.start()
                self.connected.append(address)
        except Exception as e:
            log.exception(e)
        finally:
            self.server_socket.close()

    def stop(self):
        log.warning('Server stopping')
        self.running = False

    def get_connected(self):
        return self.connected.copy()

    def on_thread_finished(self, address):
        if address in self.connected:
            self.connected.remove(address)

    def set_position(self, position):
        self.position = position

    def get_position(self):
        return self.position

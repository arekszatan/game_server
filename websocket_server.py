import socket
import threading
import time
from settings import *


class SocketServer(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.running = bool
        self.server_socket = socket.socket()
        self.server_socket.bind((SERVER, PORT))
        self.server_socket.listen(ACCESSIBLE_CONNECTION)

    def run(self) -> None:
        print(f'Server started')
        self.running = True
        conn = None
        try:
            while self.running:
                print(f'Waiting for new Connection...')
                conn, address = self.server_socket.accept()  # accept new connection
                print(f'Connected with: {address}')
                t = threading.Thread(target=self.threaded_client, args=[conn])
                t.start()
        except KeyboardInterrupt:
            print("SDadas")
            if conn:
                conn.close()
            print("Searching for chat members failed! Is the system shutting down?")

    def stop(self):
        print(f'Server stopped')
        self.running = False

    def threaded_client(self, conn):
        while True:
            try:
                data = conn.recv(1024).decode()
                if not data:
                    # print("sdadssdadsadas")
                    conn.send(str.encode("Goodbye"))
                    break
                elif data == "ping":
                    # print("pinf")
                    conn.send("pong".encode())

                else:
                    ...
                    # print("Recieved: " + reply)
                    # arr = reply.split(":")
                    # id = int(arr[0])
                    # pos[id] = reply
                    #
                    # if id == 0:
                    #     nid = 1
                    #
                    # if id == 1:
                    #     nid = 0
                    #
                    # reply = pos[nid][:]
                    # print("Sending: " + reply)

                    conn.send(data.encode())
            except:
                break

        print("Connection Closed")
        conn.close()




server = SocketServer()
server.start()
# print("sadsa")
# time.sleep(1)
# print(f'Count of thred is {len(threading.enumerate())}')
# sock2 = SocketServer()
# sock2.start()
# time.sleep(1)
# print(f'Count of thred is {len(threading.enumerate())}')
# sock2.stop()
# time.sleep(2)
# print(f'Count of thred is {len(threading.enumerate())}')
# for thread in threading.enumerate():
#     print(thread.name)
# class Test:
#     def __init__(self):
#         ...
#
#     def main(self):
#         while 1:
#             time.sleep(0.00000000000000000000000000000000000000000000001)
#             t = time.time()
#             print(t)
#
#
# test = Test()
# # tr = threading.Thread(target=test.main)
# # tr.start()
#
#
# def threaded_client(conn):
#     while True:
#         try:
#             data = conn.recv(1024).decode()
#             if not data:
#                 print("sdadssdadsadas")
#                 conn.send(str.encode("Goodbye"))
#                 break
#             elif data == "ping":
#                 print("pinf")
#                 conn.send("pong".encode())
#
#             else:
#                 ...
#                 # print("Recieved: " + reply)
#                 # arr = reply.split(":")
#                 # id = int(arr[0])
#                 # pos[id] = reply
#                 #
#                 # if id == 0:
#                 #     nid = 1
#                 #
#                 # if id == 1:
#                 #     nid = 0
#                 #
#                 # reply = pos[nid][:]
#                 # print("Sending: " + reply)
#
#                 conn.send(data.encode())
#         except:
#             break
#
#     print("Connection Closed")
#     conn.close()
#
#
# while True:
#     conn, address = server_socket.accept()  # accept new connection
#     print("Connected to: ", address)
#     t = threading.Thread(target=threaded_client, args=[conn,])
#     t.start()
#

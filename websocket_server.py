import socket
import threading
import time

from settings import *
from threading import *
import sys

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
# server_ip = socket.gethostbyname(SERVER)
# print(server_ip)
# try:
#     s.bind((SERVER, PORT))
#
# except socket.error as e:
#     print(str(e))
# host = socket.gethostname()
server_socket = socket.socket()
server_socket.bind((SERVER, PORT))

server_socket.listen(2)
print("Waiting for a connection")

currentId = "0"
pos = ["0:50,50", "1:100,100"]


class Test:
    def __init__(self):
        ...

    def main(self):
        while 1:
            t = time.time()
            # print(t)

test = Test()
tr = threading.Thread(target=test.main)
tr.start()


def threaded_client(conn):
    print("Sadsda")
    global currentId, pos
    #conn.send(str.encode(currentId))
    currentId = "1"
    reply = ''
    while True:
        try:
            data = conn.recv(1024).decode()
            print(data)
            if not data:
                print("sdadssdadsadas")
                conn.send(str.encode("Goodbye"))
                break
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


while True:
    conn, address = server_socket.accept()  # accept new connection
    print("Connected to: ", address)
    t = threading.Thread(target=threaded_client, args=[conn,])
    t.start()


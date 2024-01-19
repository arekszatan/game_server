import json
from ThreadClientBase import ThreadClientBase, socket_method
import logging as log


class GameServer(ThreadClientBase):
    def __init__(self, parent, conn, address):
        ThreadClientBase.__init__(self, parent, conn, address)
        self.is_connected_with_game_room = False
        self.bullets_position = []
        self.my_position = 0
        self.my_score = 0
        self.next_score = True

    @socket_method
    def position_after_move(self, message, prefix):
        self.my_position = int(message)
        enemy = self.parent.game_rooms.get_enemy(self)
        message_out = {
            "prefix": prefix,
            "callback_for_all": None,
            "data": self.my_position
        }
        self.send_data(json.dumps(message_out))
        message_out = {
            "prefix": 100,
            "callback_for_all": "set_enemy_position",
            "data": self.my_position
        }
        enemy.send_data(json.dumps(message_out))

    def send_score(self):
        enemy = self.parent.game_rooms.get_enemy(self)
        data = [self.my_score, enemy.my_score]
        data_enemy = [enemy.my_score, self.my_score]
        message_out = {
            "prefix": 102,
            "callback_for_all": "send_score",
            "data": data
        }
        mess_out_enemy = {
            "prefix": 102,
            "callback_for_all": "send_score",
            "data": data_enemy
        }
        enemy.send_data(json.dumps(mess_out_enemy))
        self.send_data(json.dumps(message_out))

    @socket_method
    def send_bullets_position(self, message, prefix):
        enemy = self.parent.game_rooms.get_enemy(self)
        self.bullets_position = message
        # for bullet_pos in self.bullets_position:
        #     print(bullet_pos[0], enemy.my_position)
        #     if enemy.my_position + 50 >= bullet_pos[0] >= enemy.my_position and self.next_score\
        #             and 50 <= bullet_pos[1] <= 100:
        #         self.my_score += 1
        #         print(self.my_score)
        #         self.bullets_position.remove(bullet_pos)
        #         self.send_score()
        #         self.next_score = False
        #         break
        #     else:
        #         self.next_score = True
        print(self.bullets_position)
        for bullet in self.bullets_position:
            if bullet[1] < 0:
                self.bullets_position.remove(bullet)
                print(self.bullets_position)
        message_out = {
            "prefix": prefix,
            "callback_for_all": None,
            "data": self.bullets_position
        }
        self.send_data(json.dumps(message_out))
        message_out = {
            "prefix": 101,
            "callback_for_all": "set_enemy_bullets",
            "data": self.bullets_position
        }
        enemy.send_data(json.dumps(message_out))

    @socket_method
    def connect_with_game_room(self, message, prefix):
        if self.parent.game_rooms.connect_exist_room(str(message), self):
            data = {
                "name_room": self.parent.game_rooms.get_room_name(self),
                "player_1": self.parent.game_rooms.get_player_1_name(self)
            }
        else:
            data = None
        message_out = {
            "prefix": prefix,
            "callback_for_all": None,
            "data": data
        }
        self.send_data(json.dumps(message_out))
        enemy = self.parent.game_rooms.get_enemy(self)
        message_out = {
            "prefix": 99,
            "callback_for_all": "set_player_name",
            "data": message
        }
        enemy.send_data(json.dumps(message_out))

    @socket_method
    def create_game_room(self, message, prefix):
        if self.parent.game_rooms.create_room(self.address[1], str(message), self):
            room_name = self.address[1]
        else:
            room_name = None
        message_out = {
            "prefix": prefix,
            "callback_for_all": None,
            "data": room_name
        }
        self.send_data(json.dumps(message_out))

    def remove_game_room(self):
        self.parent.game_rooms.delete_room(self)
        log.info(f'Delete room with name {self.address[1]}')





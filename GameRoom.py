import logging as log


class GameRooms:
    def __init__(self):
        self.rooms = []

    def create_room(self, owner, player_name, player):
        for room in self.rooms:
            if room.get_room_name() == owner:
                return False
        self.rooms.append(Room(owner, player_name, player))
        log.info(f'Created room with name {owner}')
        return True

    def delete_room(self, player):
        for room in self.rooms:
            if room.get_player_2() == player or room.get_player_1() == player:
                self.rooms.remove(room)

    def connect_exist_room(self, player_name, player):
        for room in reversed(self.rooms):
            if room.add_player(player_name, player):
                return True
        return False

    def get_player_1_name(self, player):
        for room in self.rooms:
            if room.get_player_2() == player or room.get_player_1() == player:
                return room.get_player_1_name()
        return None

    def get_player_2_name(self, player):
        for room in self.rooms:
            if room.get_player_2() == player or room.get_player_1() == player:
                return room.get_player_2_name()
        return None

    def get_player_1(self, player):
        for room in self.rooms:
            if room.get_player_2() == player or room.get_player_1() == player:
                return room.get_player_1()
        return None

    def get_player_2(self, player):
        for room in self.rooms:
            if room.get_player_2() == player or room.get_player_1() == player:
                return room.get_player_2()
        return None

    def get_room_name(self, player):
        for room in self.rooms:
            if room.get_player_2() == player or room.get_player_1() == player:
                return room.get_room_name()
        return None

    def get_enemy(self, player):
        for room in self.rooms:
            if room.get_player_1() == player:
                return room.get_player_2()
            if room.get_player_2() == player:
                return room.get_player_1()
        return None


class Room:
    def __init__(self, name, player_name, player):
        self.name = name
        self.player1_name = player_name
        self.player1 = player
        self.player2_name = None
        self.player2 = None

    def add_player(self, player_name, player):
        if self.player2 is None:
            self.player2 = player
            self.player2_name = player_name
            return True
        return False

    def get_player_1_name(self):
        return self.player1_name

    def get_player_2_name(self):
        return self.player2_name

    def get_player_1(self):
        return self.player1

    def get_player_2(self):
        return self.player2

    def get_room_name(self):
        return self.name



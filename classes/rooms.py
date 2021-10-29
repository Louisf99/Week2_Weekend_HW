class Room:
    def __init__(self, room_name, room_capacity):
        self.room_name = room_name
        self.room_capacity = room_capacity
        self.guest_in_room = []
        self.playlist = []

        
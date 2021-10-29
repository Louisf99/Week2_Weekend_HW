class Room:
    def __init__(self, room_name, room_capacity):
        self.room_name = room_name
        self.room_capacity = room_capacity
        self.guest_in_room = []
        self.playlist = []

    def check_in_to_room(self, guest):
            if len(self.guest_in_room) < self.room_capacity:
                self.guest_in_room.append(guest)
                return True
            return False


    def check_out_of_room(self, guest):
        self.guest_in_room.remove(guest)

    
    

class Room:
    def __init__(self, room_name, room_capacity):
        self.room_name = room_name
        self.room_capacity = room_capacity
        self.guest_in_room = []
        self.playlist = []

    def check_in_to_room(self, guest):
        self.guest_in_room.append(guest)
    # def check_in_to_room(self, guest):
    #     if len(self.guest_in_room) < self.room_capacity:
    #         self.guest_in_room.append(guest)
    #         print("welcome have a nice time")
    #     else:
    #         if len(self.guest_in_room) == self.room_capacity:
    #             print("room is full")
                
    def check_out_of_room(self, guest):
        self.guest_in_room.remove(guest)

    def add_song(self, song):
        self.playlist.append(song)

    def remove_song(self, song):
        self.playlist.remove(song)



    
   
import unittest
from classes.rooms import Room
from classes.guests import Guest
from classes.songs import Song

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room1 = Room("LED Room",10 )
        self.room2 = Room("Pop Room", 12)
        self.room3 = Room("VIP Room", 4)

        self.guest1 = Guest("Harry", 35, "White Noise")
        self.guest2 = Guest("Liam", 50, "Ticket To Ride")
        self.guest3 = Guest("Susan", 75, "American Boy")
        self.guest4 = Guest("Ben", 13, "Bank Account")
        self.guest5 = Guest("Jack", 22, "Watermelon Sugar")
        
        self.song1 = Song("White Noise", "Disclosure, Aluna George")
        self.song2 = Song("White Iverson", "Post Malone")
        self.song3 = Song("Durag Activity", "Baby Keem, Travis Scott")
        

    def test_room_has_room_name(self):
        self.assertEqual("LED Room", self.room1.room_name)

    def test_room_has_room_name2(self):
        self.assertEqual("Pop Room", self.room2.room_name)

    def test_room_has_room_name3(self):
        self.assertEqual("VIP Room", self.room3.room_name)

    def test_room_has_room_capacity(self):
        self.assertEqual(10, self.room1.room_capacity)

    def test_room_has_room_capacity2(self):
        self.assertEqual(12, self.room2.room_capacity)
        
    def test_room_has_room_capacity3(self):
        self.assertEqual(4, self.room3.room_capacity)

    def test_room_has_no_guest_in_room(self):
        self.assertEqual(0,len(self.room1.guest_in_room))

    def test_room_has_no_guest_in_room2(self):
        self.assertEqual(0,len(self.room2.guest_in_room))

    def test_room_has_no_guest_in_room3(self):
        self.assertEqual(0,len(self.room3.guest_in_room))

    def test_check_in_to_room1_works(self):
        self.room1.check_in_to_room(self.guest1)
        self.assertEqual(1, len(self.room1.guest_in_room))

    def test_check_in_to_room2_works(self):
        self.room2.check_in_to_room(self.guest2)
        self.assertEqual(1, len(self.room2.guest_in_room))

    def test_check_in_to_room3_works(self):
        self.room3.check_in_to_room(self.guest3)
        self.assertEqual(1, len(self.room3.guest_in_room))

    
    



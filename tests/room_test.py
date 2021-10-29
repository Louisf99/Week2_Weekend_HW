import unittest
from classes.rooms import Room
from classes.guests import Guest
from classes.songs import Song

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room1 = Room("LED Room",40 )
        self.room2 = Room("Pop Room", 50)
        self.room3 = Room("VIP Room", 20)

        self.guest1 = Guest("harry", 35, "White Noise")
        self.guest2 = Guest("Liam", 50, "Ticket To Ride")
        self.guest3 = Guest("Susan", 75, "American Boy")
        
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
        self.assertEqual(40, self.room1.room_capacity)

    def test_room_has_room_capacity2(self):
        self.assertEqual(50, self.room2.room_capacity)
        
    def test_room_has_room_capacity3(self):
        self.assertEqual(20, self.room3.room_capacity)
        

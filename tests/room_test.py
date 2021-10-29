import unittest
from classes.rooms import Room
from classes.guests import Guest
from classes.songs import Song

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.guest1 = Guest("harry", 35, "White Noise")
        self.guest2 = Guest("Liam", 50, "Ticket To Ride")
        self.guest3 = Guest("Susan", 75, "American Boy")
        
        self.room1 = Room("LED Room",40 )
        self.room2 = Room("Pop Room", 50)
        self.room3 = Room("VIP Room", 20)

        self.song1 = Song("White Noise", "Disclosure, Aluna George")
        self.song2 = Song("White Iverson", "Post Malone")
        self.song3 = Song("Durag Activity", "Baby Keem, Travis Scott")
        
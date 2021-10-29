import unittest
from classes.guests import Guest
from classes.rooms import Room

class TestGuest(unittest.TestCase):
    
    def setUp(self):
        self.guest1 = Guest("Harry", 35, "White Noise")
        self.guest2 = Guest("Liam", 50, "Ticket To Ride")
        self.guest3 = Guest("Susan", 75, "American Boy")
        
        self.room1 = Room("LED Room",40 )
        self.room2 = Room("Pop Room", 50)
        self.room3 = Room("VIP Room", 20)


    def test_guest_has_name(self):
        self.assertEqual("Harry", self.guest1.name)

    def test_guest_has_name2(self):
        self.assertEqual("Liam", self.guest2.name)
    
    def test_guest_has_name3(self):
        self.assertEqual("Susan", self.guest3.name)

    def test_guest_has_cash(self):
        self.assertEqual(35, self.guest1.wallet)
    
    def test_guest_has_cash2(self):
        self.assertEqual(50, self.guest2.wallet)
    
    def test_guest_has_cash3(self):
        self.assertEqual(75, self.guest3.wallet)
    
    def test_guest_has_favourite_song(self):
        self.assertEqual("White Noise", self.guest1.favourite_song)

    def test_guest_has_favourite_song2(self):
        self.assertEqual("Ticket To Ride", self.guest2.favourite_song)

    def test_guest_has_favourite_song3(self):
        self.assertEqual("American Boy", self.guest3.favourite_song)


     


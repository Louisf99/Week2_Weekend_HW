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

    
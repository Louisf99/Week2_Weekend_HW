import unittest
from classes.guests import Guest
from classes.rooms import Room

class TestGuest(unittest.TestCase):
    def setUp(self):
        guest1 = ("harry", 35)
        guest2 = ("Liam", 50)
        guest3 = ("Susan", 75)
        guest4 = ("Craig", 20)
        
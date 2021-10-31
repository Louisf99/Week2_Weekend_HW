import unittest
from classes.guests import Guest
from classes.songs import Song

class TestGuest(unittest.TestCase):
    
    def setUp(self):
        self.guest1 = Guest("Harry", 35, "White Noise")
        self.guest2 = Guest("Liam", 50, "Ticket To Ride")
        self.guest3 = Guest("Susan", 75, "American Boy")
        self.guest4 = Guest("Ben", 13, "Bank Account")
        self.guest5 = Guest("Jack", 22, "Watermelon Sugar")

        self.song1 = Song("White Noise", "Disclosure, Aluna George")
        self.song2 = Song("White Iverson", "Post Malone")
        self.song3 = Song("Durag Activity", "Baby Keem, Travis Scott")


    def test_guest_has_name(self):
        self.assertEqual("Harry", self.guest1.name)

    def test_guest_has_name2(self):
        self.assertEqual("Liam", self.guest2.name)
    
    def test_guest_has_name3(self):
        self.assertEqual("Susan", self.guest3.name)

    def test_guest_has_name4(self):
        self.assertEqual("Ben", self.guest4.name)

    def test_guest_has_name5(self):
        self.assertEqual("Jack", self.guest5.name)

    def test_guest_has_cash(self):
        self.assertEqual(35, self.guest1.wallet)
    
    def test_guest_has_cash2(self):
        self.assertEqual(50, self.guest2.wallet)
    
    def test_guest_has_cash3(self):
        self.assertEqual(75, self.guest3.wallet)

    def test_guest_has_cash4(self):
        self.assertEqual(13, self.guest4.wallet)

    def test_guest_has_cash5(self):
        self.assertEqual(22, self.guest5.wallet)
    
    def test_guest_has_favourite_song(self):
        self.assertEqual("White Noise", self.guest1.favourite_song)

    def test_guest_has_favourite_song2(self):
        self.assertEqual("Ticket To Ride", self.guest2.favourite_song)

    def test_guest_has_favourite_song3(self):
        self.assertEqual("American Boy", self.guest3.favourite_song)

    def test_guest_has_favourite_song4(self):
        self.assertEqual("Bank Account", self.guest4.favourite_song)

    def test_guest_has_favourite_song5(self):
        self.assertEqual("Watermelon Sugar", self.guest5.favourite_song)

    # def test_guest_does_not_cheer(self):
    #     playlist = [self.song2, self.song3]
    #     self.assertEqual(None, self.guest1.favourite_song(playlist))


     


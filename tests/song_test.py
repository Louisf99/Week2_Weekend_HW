import unittest
from classes.songs import Song
from classes.rooms import Room

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song1 = Song("White Noise", "Disclosure, Aluna George")
        self.song2 = Song("White Iverson", "Post Malone")
        self.song3 = Song("Durag Activity", "Baby Keem, Travis Scott")
        


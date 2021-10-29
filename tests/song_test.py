import unittest
from classes.songs import Song

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song1 = Song("White Noise", "Disclosure, Aluna George")
        self.song2 = Song("White Iverson", "Post Malone")
        self.song3 = Song("Durag Activity", "Baby Keem, Travis Scott")
        

    def test_song_has_song_name(self):
        self.assertEqual("White Noise", self.song1.song_name)

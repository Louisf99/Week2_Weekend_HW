import unittest
from classes.songs import Song

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song1 = Song("White Noise", "Disclosure, Aluna George")
        self.song2 = Song("White Iverson", "Post Malone")
        self.song3 = Song("Durag Activity", "Baby Keem, Travis Scott")
        

    def test_song_has_song_name(self):
        self.assertEqual("White Noise", self.song1.song_name)
    
    def test_song_has_song_name2(self):
        self.assertEqual("White Iverson", self.song2.song_name)
    
    def test_song_has_song_name3(self):
        self.assertEqual("Durag Activity", self.song3.song_name)

    def test_song_has_artist_name(self):
        self.assertEqual("Disclosure, Aluna George", self.song1.artist_name)

    def test_song_has_artist_name2(self):
        self.assertEqual("Post Malone", self.song2.artist_name)
        
    def test_song_has_artist_name3(self):
        self.assertEqual("Baby Keem, Travis Scott", self.song3.artist_name)
        


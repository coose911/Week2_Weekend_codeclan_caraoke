import unittest

from classes.song import *


class TestSong(unittest.TestCase):
    def setUp(self):
        self.song_1 = Song("deadmau5", "ghosts n stuff")
        self.song_2 = Song("titanium", "david guetta")
        self.song_3 = Song("i know", "arc north")

    def test_song_name(self):
        self.assertEqual("ghosts n stuff", self.song_1.song_name)

    def test_artist(self):
        self.assertEqual("deadmau5", self.song_1.artist)

    def test_song_name(self):
        self.assertEqual("arc north", self.song_3.song_name)

    def test_artist(self):
        self.assertEqual("i know", self.song_3.artist)


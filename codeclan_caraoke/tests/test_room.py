import unittest

from classes.room import Room


class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room_1 = Room("porter", True, False)
        self.five_pound = 5
        self.add_song1 = self.room_1.add_song_to_room("god of ages")
        self.add_song2 = self.room_1.add_song_to_room("titanium")
        self.room_1.add_guest_to_room(Room("porter", True, False))
        self.room_1.add_guest_to_room(Room("katie", True, False))
        self.room_1.add_guest_to_room(Room("kayliegh", True, False))


    def test_check_guest(self):
        self.assertEqual("porter", self.room_1.guest)

    def test_guest_check_in(self):
        self.assertEqual(True, self.room_1.check_in)

    def test_guest_check_out(self):
        self.assertEqual(False, self.room_1.check_out)

    def test_adding_song(self):
        self.assertEqual(["god of ages", "titanium"], self.room_1.songs)

    def test_add_guest_to_room(self):
        self.assertEqual(3, len(self.room_1.guests))

    def test_number_of_guests_in_room(self):
        self.assertEqual(3, self.room_1.number_of_guests_in_room())

    def test_room_is_full(self):
        self.assertEqual("room full", self.room_1.room_is_full())

    def test_charge_customer(self):
        self.room_1.charge_customer(self.five_pound)
        till_amount = self.room_1.till
        self.assertEqual(5, till_amount)

    def test_customers_favourite_song(self):
        self.fav_song = self.room_1.customer_favourite_song('titanium')
        self.assertEqual("woop! this is my favourite song", self.fav_song)
    
    def test_remove_guest_from_room(self):
        self.room_1.remove_guests_from_room()
        self.assertEqual([], self.room_1.guests)

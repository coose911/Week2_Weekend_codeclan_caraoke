import unittest

from classes.guest import Guest

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest_1 = Guest("porter", 30, 100)
        self.guest_2 = Guest("robin", 27, 120)


    def test_guest_name(self):
        self.assertEqual("Porter", self.guest_1.name)

    def test_guest_age(self):
        self.assertEqual(30, self.guest_1.age)

    def test_guest_name(self):
        self.assertEqual("robin", self.guest_2.name)

    def test_guest_age(self):
        self.assertEqual(27, self.guest_2.age)

    def test_reduce_wallet_of_guest_1(self):
        self.charged_five_pounds = 5
        self.assertEqual(95, self.guest_1.reduce_wallet(self.charged_five_pounds))
    
    def test_reduce_wallet_of_guest_2(self):
        self.charged_five_pounds = 5
        self.assertEqual(115, self.guest_2.reduce_wallet(self.charged_five_pounds))
    



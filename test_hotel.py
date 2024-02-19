"""Module for Unit Testing hotel module"""

import unittest
import os
import io
from unittest.mock import patch
from hotel import Hotel


class TestHotel(unittest.TestCase):
    """Class to perform Hotel unit tests"""
    def setUp(self):
        """Method for SetUp"""
        self.hotel = Hotel(name='setup',
                           rating=5, rooms={'101': True, '102': False})

    def test_hotel_init(self):
        """Method to verify initialization"""
        self.assertEqual(self.hotel.name, 'setup')
        self.assertEqual(self.hotel.rating, 5)
        self.assertEqual(self.hotel.rooms, {'101': True, '102': False})

    def test_create_hotel(self):
        """Method to verify hotel creation"""
        Hotel.create_hotel('create_test', 5, {'201': True})
        expected_filename = "hotel_create_test.json"
        self.assertTrue(os.path.exists(expected_filename),
                        "Hotel file should exist")
        os.remove("hotel_create_test.json")

    def test_load_file(self):
        """Method to verify hotel loading"""
        load_test_hotel = Hotel.create_hotel('load_test', 4, {'301': True})
        loaded_hotel = Hotel.load_hotel('load_test')

        self.assertEqual(loaded_hotel.name, load_test_hotel.name,
                         "Hotel names should be the same")
        self.assertEqual(loaded_hotel.rating, load_test_hotel.rating,
                         "Ratings should be the same")
        self.assertEqual(loaded_hotel.rooms, load_test_hotel.rooms,
                         "Rooms should be the same")
        os.remove("hotel_load_test.json")

    def test_delete_hotel(self):
        """Method to verify hotel deletion"""
        Hotel.create_hotel('delete_test', 3, {'404': True})
        expected_filename = "hotel_delete_test.json"
        self.assertTrue(os.path.exists(expected_filename),
                        "Hotel file should exist")

        Hotel.delete_hotel('delete_test')
        self.assertFalse(os.path.exists(expected_filename),
                         "Hotel file should no longer exist")

    def test_display_hotel(self):
        """Method to verify display"""
        hotel = Hotel('display_test', 5, {'505': True})
        disp = "Hotel: display_test, Stars: 5, Rooms: {'505': True}\n"

        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            hotel.display_hotel()
            self.assertEqual(fake_out.getvalue(), disp,
                             "The displayed information should be the same")

    def test_update_hotel(self):
        """Method to verify update"""
        new_name = 'Updated Name'
        new_rating = 4

        self.hotel.update_hotel(new_name, new_rating)

        self.assertEqual(self.hotel.name, new_name)
        self.assertEqual(self.hotel.rating, new_rating)

    def test_reserve_room(self):
        """Method to verify room reservation"""
        hotel = Hotel('reserve_test', 5, {'777': True})
        available = hotel.rooms.get('777')
        self.assertTrue(available)

        hotel.reserve_room('777')
        new_available = hotel.rooms.get('777')
        self.assertFalse(new_available)


if __name__ == '__main__':
    unittest.main()

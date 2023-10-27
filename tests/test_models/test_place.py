#!/usr/bin/python3
"""Tests for place."""

import unittest
from models.place import Place


class TestPlaceAttributes(unittest.TestCase):
    def test_latitude_float(self):
        """Test that the 'latitude' attribute is a float."""
        place = Place()
        self.assertIsInstance(place.latitude, float)

    def test_longitude_float(self):
        """Test that the 'longitude' attribute is a float."""
        place = Place()
        self.assertIsInstance(place.longitude, float)

    def test_number_rooms_integer(self):
        """
        Test that the 'number_rooms' attribute is an integer
        and initialized in 0.
        """
        place = Place()
        self.assertIsInstance(place.number_rooms, int)
        self.assertEqual(place.number_rooms, 0)

    def test_number_bathrooms_integer(self):
        """Test that the 'number_bathrooms' attribute is an integer
        and initialized in 0.
        """
        place = Place()
        self.assertIsInstance(place.number_bathrooms, int)
        self.assertEqual(place.number_bathrooms, 0)

    def test_max_guest_integer(self):
        """Test that the 'max_guest' attribute is an integer
        and initialized in 0.
        """
        place = Place()
        self.assertIsInstance(place.max_guest, int)
        self.assertEqual(place.max_guest, 0)

    def test_price_by_night_integer(self):
        """Test that the 'price_by_night' attribute is an integer
        and initialized in 0.
        """
        place = Place()
        self.assertIsInstance(place.price_by_night, int)
        self.assertEqual(place.price_by_night, 0)

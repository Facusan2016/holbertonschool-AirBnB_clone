#!/usr/bin/python3
"""Test for city."""

import unittest
from models.city import City


class TestCityAttributes(unittest.TestCase):
    def test_name_empty_string(self):
        """Test if the 'name' attribute is an empty string."""
        city = City()
        self.assertEqual(city.name, "")

    def test_state_id_empty_string(self):
        """Test if the 'state_id' attribute is an empty string."""
        city = City()
        self.assertEqual(city.state_id, "")

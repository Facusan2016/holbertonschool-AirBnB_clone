#!/usr/bin/python3
"""Test amenity."""

import unittest
from models.amenity import Amenity


class TestAmenityAttributes(unittest.TestCase):
    def test_name_empty_string(self):
        """Test if the 'name' attribute is an empty string."""
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

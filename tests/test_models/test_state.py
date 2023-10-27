#!/usr/bin/python3
"""Test for state."""


import unittest
from models.state import State


class TestStateAttributes(unittest.TestCase):
    def test_name_empty_string(self):
        """Test if the 'name' attribute is an empty string."""
        state = State()
        self.assertEqual(state.name, "")

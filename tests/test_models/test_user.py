#!/usr/bin/python3
"""Tests for user."""

import unittest
from models.user import User


class TestUserAttributes(unittest.TestCase):
    def test_email_empty_string(self):
        """Test if 'email' attribute is an empty string."""
        user = User()
        self.assertEqual(user.email, "")

    def test_password_empty_string(self):
        """Test if 'password' attribute is an empty string."""
        user = User()
        self.assertEqual(user.password, "")

    def test_first_name_empty_string(self):
        """Test if 'first_name' attribute is an empty string."""
        user = User()
        self.assertEqual(user.first_name, "")

    def test_last_name_empty_string(self):
        """Test if 'last_name' attribute is an empty string."""
        user = User()
        self.assertEqual(user.last_name, "")

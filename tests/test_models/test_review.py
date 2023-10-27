#!/usr/bin/python3
"""Tests for review."""

import unittest
from models.review import Review
from models.place import Place
from models.user import User


class TestReviewAttributes(unittest.TestCase):
    def test_place_id_empty_string(self):
        """Test if 'place_id' attribute is an empty string."""
        review = Review()
        self.assertEqual(review.place_id, "")

    def test_user_id_empty_string(self):
        """Test if 'user_id' attribute is an empty string."""
        review = Review()
        self.assertEqual(review.user_id, "")

    def test_text_empty_string(self):
        """Test if 'text' attribute is an empty string."""
        review = Review()
        self.assertEqual(review.text, "")

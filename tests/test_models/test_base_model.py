#!/usr/bin/python3

import unittest
import time
from models.base_model import BaseModel

"""
    In this module we're testing the BaseModel
    basics attributes and methods

"""


class TestBaseModelClass(unittest.TestCase):

    """Tests for BaseModel class"""

    def testIdString(self):
        """Checks if id is a string"""
        a = BaseModel()
        self.assertEqual(type(a.id), str)

    def testUniqueId(self):
        """Checks if the id is unique"""
        a = BaseModel()
        b = BaseModel()
        self.assertNotEqual(a.id, b.id)

    def testCreatedTime(self):
        """
            Checks if the created_at time is greater
            than updated time.
        """
        a = BaseModel()
        time.sleep(1)
        a.save()
        self.assertTrue(a.created_at < a.updated_at)

    def testStrRepresentation(self):
        """Checks if the str representation is correct"""
        a = BaseModel()
        a_repr = a.__str__()
        r_str = f"[{type(a).__name__}] ({a.id}) {a.__dict__}"
        self.assertEqual(a_repr, r_str)

    def testToDict(self):
        """
            Checks if the to_dict method returns the correct key/value
            pairs.
        """
        a = BaseModel()
        res_dict = a.__dict__.copy()
        res_dict.update(__class__=type(a).__name__)
        res_dict.update(created_at=a.created_at.isoformat())
        res_dict.update(updated_at=a.updated_at.isoformat())
        self.assertEqual(res_dict, a.to_dict())
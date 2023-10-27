#!/usr/bin/python3

import unittest
import os
from models.base_model import BaseModel
from models import storage
from unittest.mock import patch


class TestFileStorage(unittest.TestCase):

    def test_dictionary_exist(self):
        """Check if the __objects dictionary exists in FileStorage."""
        self.assertTrue(hasattr(storage, '_FileStorage__objects'))

    def test_key_format(self):
        """Check if the key format is "classname.id"""
        base_model = BaseModel()

        key = f"{type(base_model).__name__}.{base_model.id}"
        self.assertEqual(key, f"BaseModel.{base_model.id}")

    def test_reload_file_existence(self):
        """"Check if reload() deserializes the file only if it exists"""
        file_path = storage._FileStorage__file_path
        if os.path.isfile(file_path):
            os.remove(file_path)
        storage.reload()

    def test_update_base_model(self):
        """Check if models/base_model.py is updated with storage"""
        with open('models/base_model.py', 'r') as base_model_file:
            base_model_contents = base_model_file.read()
            self.assertIn("from models import storage", base_model_contents)

    def test_init_new_instance(self):
        """Check if BaseModel's __init__ creates a new instance"""
        base_model = BaseModel()
        key = f"{type(base_model).__name__}.{base_model.id}"
        self.assertIn(key, storage.all())

    def test_save_method(self):
        """Test if save method calls save method of storage."""
        obj = BaseModel()
        with unittest.mock.patch.object(storage, 'save') as mock_save:
            obj.save()
            mock_save.assert_called_once()

    def test_new_method(self):
        """Test if new method calls new method of storage."""
        obj = BaseModel()
        with unittest.mock.patch.object(storage, 'new') as mock_new:
            obj.__init__()
            mock_new.assert_called_once_with(obj)

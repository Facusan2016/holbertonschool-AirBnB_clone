#!/usr/bin/python3

"""This module defines the base_model class."""

import uuid
from datetime import datetime


class BaseModel:
    """BaseModel class."""

    def __init__(self):
        """Init method to BaseModel"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """String representation of a BaseModel"""
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Method that updates the created_at attribute"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Method that returns the dict representation of the Object"""
        new_dict = self.__dict__.copy()
        new_dict.update(__class__=type(self).__name__)
        new_dict.update(created_at=self.created_at.isoformat())
        new_dict.update(updated_at=self.updated_at.isoformat())
        return new_dict

#!/usr/bin/python3

"""This module defines the base_model class."""

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """BaseModel class."""

    def __init__(self, *args, **kwargs):
        """Init method to BaseModel"""
        special_args_keys = ('created_at', 'updated_at')

        if len(kwargs) > 0:
            for k, v in kwargs.items():
                if k == '__class__':
                    continue
                if k in special_args_keys:
                    format = "%Y-%m-%dT%H:%M:%S.%f"
                    self.__setattr__(k, datetime.strptime(v, format))
                else:
                    self.__setattr__(k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """String representation of a BaseModel"""
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Method that updates the created_at attribute"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Method that returns the dict representation of the Object"""
        new_dict = self.__dict__.copy()
        new_dict.update(__class__=type(self).__name__)
        new_dict.update(created_at=self.created_at.isoformat())
        new_dict.update(updated_at=self.updated_at.isoformat())
        return new_dict

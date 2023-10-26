#!/usr/bin/python3

from models.base_model import BaseModel

"""Declaration of user class"""


class User(BaseModel):
    """User class implementation"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

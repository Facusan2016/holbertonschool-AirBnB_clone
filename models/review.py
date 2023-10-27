#!/usr/bin/python3

from models.base_model import BaseModel

"""Declaration of review class"""


class Review(BaseModel):
    """Define the Review class."""
    name = ""
    place_id = ""
    user_id = ""
    text = ""

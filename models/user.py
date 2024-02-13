#!/usr/bin/python3
"""A module that inherits the BaseModel"""


from models.basemodel import BaseModel

class User(BaseModel):
    """A class that defines a new user"""

    def __init__(self):
        """To initialize new variables"""

        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""

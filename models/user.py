#!/usr/bin/python3
"""A module that inherits the BaseModel"""


from models.base_model import BaseModel

class User(BaseModel):
    """A class that defines a new user"""

    def __init__(self, *args, **kwargs):
        """To initialize new variables"""

        if len(kwargs) > 0:
            super().__init__(**kwargs)
        else:
            super().__init__()
            self.email = ""
            self.password = ""
            self.first_name = ""
            self.last_name = ""

#!/usr/bin/python3
"""A module to define a class BaseModel"""

import uuid
from datetime import date
from datetime import datetime


class BaseModel:
    """The super class"""

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

    def __str__(self):
        """To provide a string representation of the class
        """
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """To update the attribute upodated at with the current\
 date and time
        """

        self.updated_at = datetime.today()

    def to_dict(self):
        """To return a dictionary of the class"""

        self.created_at = self.created_at.isoformat()
        self.updated_at = self.updated_at.isoformat()
        self.__dict__.update({'__class__': type(self).__name__})
        return self.__dict__

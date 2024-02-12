#!/usr/bin/python3
"""A module to define a class BaseModel"""

import uuid
from datetime import datetime
from models.__init__ import storage


class BaseModel:
    """The super class"""

    def __init__(self, *args, **kwargs):
        """A function to initialize the class
        Args:
            args (list): a list of variables passed to the function
            kwargs (dict): a dictionary passed to the function
            """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if kwargs is not None:
            for a, b in kwargs.items():
                if a == '__class__':
                    continue
                elif a == 'created_at' or a == 'updated_at':
                    setattr(self, a, datetime.fromisoformat(b))
                    continue
                setattr(self, a, b)
        else:
            obj = self.to_dict()
            storage.new(obj)

    def __str__(self):
        """To provide a string representation of the class
        """
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """To update the attribute upodated at with the current\
 date and time
        """

        self.updated_at = datetime.today()
        storage.save()

    def to_dict(self):
        """To return a dictionary of the class"""

        self.created_at = self.created_at.isoformat()
        self.updated_at = self.updated_at.isoformat()
        self.__dict__.update({'__class__': type(self).__name__})
        return self.__dict__

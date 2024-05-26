#!/usr/bin/python3
"""A module to define a class BaseModel"""

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """The super class"""

    def __init__(self, *args, **kwargs):
        """A function to initialize the class
        Args:
            args (list): a list of variables passed to the function
            kwargs (dict): a dictionary passed to the function
            """
        if len(kwargs) > 0:
            for a, b in kwargs.items():
                if a == '__class__':
                    continue
                elif a == "created_at" or a == "updated_at":
                    b = datetime.fromisoformat(b)
                    setattr(self, a, b)
                else:
                    setattr(self, a, b)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.today()
            a = self.to_dict()
            storage.new(a)

    def __str__(self):
        """To provide a string representation of the class
        """
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """To update the attribute upodated at with the current\
 date and time
        """

        self.updated_at = datetime.today()
        a = self.to_dict()
        storage.new(a)
        storage.save()

    def to_dict(self):
        """To return a dictionary of the class"""

        a = {}
        for key, value in self.__dict__.items():
            a[key] = value
        b = a['created_at']
        a['created_at'] = b.isoformat()
        b = a['updated_at']
        a['updated_at'] = b.isoformat()
        a.update({'__class__': type(self).__name__})
        return a

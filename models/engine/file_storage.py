#!/usr/bin/python3
"""A module to serialize and deserialize an instance to JSON file
"""


import json


class FileStorage:
    """A class that stores the information of a  BaseModel class

    """

    def __init__(self):
        """A function to create file attributes"""
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """ A function to return the private attribute objects
        """

        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        new_object = {}
        for key, value in self.__objects.items():
            a = key.split('.')
            if a[0] == "BaseModel":
                my_model = BaseModel(**value)
            elif a[0] == "User":
                my_model = User(**value)
            elif a[0] == "State":
                my_model = State(**value)
            elif a[0] == "City":
                my_model = City(**value)
            elif a[0] == "Amenity":
                my_model = Amenity(**value)
            elif a[0] == "Review":
                my_model = Review(**value)
            new_object[key] = my_model

        return new_object

    def new(self, obj):
        """A function to define the obj of the class
        Args:
            obj (dict): a dictionary of the Airbnb clone
        """
        a = "{}.{}".format(obj["__class__"], obj['id'])
        self.__objects[a] = obj

    def save(self):
        """To serialize an object to json file
        """
        with open(self.__file_path, mode='w', encoding="utf-8") as a:
            a.write(json.dumps(self.__objects))

    def reload(self):
        """A function to deserialize a json file"""
        try:
            with open(self.__file_path, mode='r', encoding="utf-8") as a:
                self.__objects = json.loads(a.read())
        except FileNotFoundError:
            pass

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

    @property
    def objects(self):
        """ A function to return the private attribute objects
        """
        return self.__objects

    @objects.setter
    def new(self, obj):
        """A function to define the obj of the class
        Args:
            obj (dict): a dictionary of the Airbnb clone
        """
        a = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[a] = obj

    def reload(self):
        """A function to deserialize a json file"""
        try:
            with open(self.__file_path, mode='r', encoding="utf-8") as a:
                self.__objects = a.read(json.loads(self.__object))
        except Exception:
            pass

    def save(self):
        """To serialize an object to json file
        """
        with open(self.__file_path, mode='w', encoding="utf-8") as a:
            a.write(json.dumps(self.__objects))

    def all(self):
        return self.__objects

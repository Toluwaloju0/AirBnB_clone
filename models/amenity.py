#!/usr/bin/python3
"""A module to define amenities"""


from models.basemodel import BaseModel

class Amenity(BaseModel):
    """A class of the city"""

    def __init__(self):
        """A function to initialize variables"""

        self.name = ""

#!/usr/bin/python3
"""A module to define a city"""


from models.basemodel import BaseModel

class City(BaseModel):
    """A class of the city"""

    def __init__(self):
        """A function to initialize variables"""

        self.state_id = ""
        self.name = ""

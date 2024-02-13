#!/usr/bin/python3
"""A module that defines a state"""


from models.basemodel import BaseModel

class state(BaseModel):
    """A class that defijnes a state"""

    def __init__(self):
        """A function to initialize variables"""

        self.name = ""

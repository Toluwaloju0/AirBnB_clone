#!/usr/bin/python3
"""A module to store reviews"""


from models.basemodel import BaseModel

class Review(BaseModel):
    """A class of the city"""

    def __init__(self):
        """A function to initialize variables"""

        self.place_id = ""
        self.user_id = ""
        self.text = ""


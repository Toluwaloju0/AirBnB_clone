#!/usr/bin/python3
"""A module to define amenities"""


from models.base_model import BaseModel

class Amenity(BaseModel):
    """A class of the city"""

    def __init__(self, *args, **kwargs):
        """A function to initialize variables"""

        if len(kwargs) > 0:
            super().__init__(**kwargs)
        else:
            super().__init__()
            self.name = ""

#!/usr/bin/python3
"""A module to define a city"""


from models.base_model import BaseModel

class City(BaseModel):
    """A class of the city"""

    def __init__(self, *args, **kwargs):
        """A function to initialize variables"""

        if len(kwargs) > 0:
            super().__init__(**kwargs)
        else:
            super().__init__()
            self.state_id = ""
            self.name = ""

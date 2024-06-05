#!/usr/bin/python3
"""A module to store reviews"""


from models.base_model import BaseModel

class Review(BaseModel):
    """A class of the city"""

    def __init__(self, *args, **kwargs):
        """A function to initialize variables"""

        if len(kwargs) > 0:
            super().__init__(**kwargs)
        else:
            super().__init__()
            self.place_id = ""
            self.user_id = ""
            self.text = ""


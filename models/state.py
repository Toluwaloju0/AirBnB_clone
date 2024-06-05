#!/usr/bin/python3
"""A module that defines a state"""


from models.base_model import BaseModel

class State(BaseModel):
    """A class that defines a state"""

    def __init__(self, *args, **kwargs):
        """A function to initialize variables"""

        if len(kwargs) > 0:
            super().__init__(**kwargs)
        else:
            super().__init__()
            self.name = ""

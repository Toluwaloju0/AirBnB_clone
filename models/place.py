#!/usr/bin/python3
"""A module to define a house detials"""


from models.base_model import BaseModel

class Place(BaseModel):
    """A class of the city"""

    def __init__(self, *args, **kwargs):
        """A function to initialize variables"""

        if len(kwargs) > 0:
            super().__init__(**kwargs)
        else:
            super().__init__()
            self.city_id = ""
            self.user_id = ""
            self.name = ""
            self.description = ""
            self.number_rooms = 0
            self.number_bathrooms = 0
            self.max_guest = 0
            self.price_by_night = 0
            self.latitude = 0.0
            self.longitude = 0.0
            self.amenity_ids = []

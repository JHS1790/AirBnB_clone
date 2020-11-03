#!/usr/bin/python3
'''file for the Amenity class'''

from . import BaseModel


class Amenity(BaseModel):
    '''Amenity'''

    name = ""

    def __init__(self):
        super().__init__()
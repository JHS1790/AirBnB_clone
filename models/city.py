#!/usr/bin/python3
'''file for the City class'''

from . import BaseModel


class City(BaseModel):
    '''City'''

    state_id = ""
    name = ""

    def __init__(self):
        super().__init__()
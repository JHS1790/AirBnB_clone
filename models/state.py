#!/usr/bin/python3
'''file for the State class'''

from . import BaseModel


class State(BaseModel):
    '''State'''

    name = ""

    def __init__(self):
        super().__init__()
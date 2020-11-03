#!/usr/bin/python3
'''file for the Review class'''

from . import BaseModel


class Review(BaseModel):
    '''Review'''

    place_id = ""
    user_id = ""
    text = ''

    def __init__(self):
        super().__init__()

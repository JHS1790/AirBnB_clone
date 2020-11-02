#!/usr/bin/python3
'''User file'''

from . import BaseModel


class User(BaseModel):
    '''Users, schmoozers'''

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self):
        super().__init__()
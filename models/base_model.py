#!/usr/bin/python3
'''file for base model class'''

from models import storage
from uuid import uuid4
from datetime import datetime


class BaseModel():
    '''All your base now belong to us

    '''

    def __init__(self, *args, **kwargs):
        '''initialize Minuteman III, or not hahahaha, unless...?

        Args:
            *args: Black Magic
            **kwargs: Even More Black Magic
                (also you should just pump a dict into this)
        '''
        if kwargs != {}:
            self.id = kwargs.get('id')
            self.created_at = (
                datetime.strptime(
                    kwargs.get('created_at'), '%Y-%m-%dT%H:%M:%S.%f'
                    )
            )
            self.updated_at = (
                datetime.strptime(
                    kwargs.get('updated_at'), '%Y-%m-%dT%H:%M:%S.%f'
                    )
            )
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        '''The string of fate has been severed,
        persist in this doomed world you have created

        Return:
            the completed print_string:
            [<class name>] (<self.id>) <self.__dict__>
        '''
        print_string = "["
        print_string += str(self.__class__.__name__)
        print_string += "] ("
        print_string += self.id
        print_string += ") "
        print_string += str(self.__dict__)
        return print_string

    def save(self):
        '''updates the public instance attribute
        updated_at with the current datetime

        '''
        updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        '''does a thing *burp*

        Return:
            new_dict, basically just __dict__ updated with
            instance class name and datetimes
        '''
        new_dict = self.__dict__
        new_dict['__class__'] = str(self.__class__.__name__)
        new_dict['created_at'] = datetime.isoformat(self.created_at)
        new_dict['updated_at'] = datetime.isoformat(self.updated_at)
        return new_dict

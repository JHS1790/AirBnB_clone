#!/usr/bin/python3
'''file for FileStorage class'''

import json
from os import path


class FileStorage():
    '''It's like a manila envelope but it looks like the Matrix Grandma.

    '''

    def __init__(self, new_path='file.json'):
        '''I dunno if this needs to be here

        '''
        self.file_path = new_path
        self.objects = {}

    def all(self):
        ''' returns the dictionary __objects

        '''
        return self.objects

    def new(self, obj):
        '''adds a new obj to objects

        '''
        working_objects = self.objects
        new_key = obj.__class__.__name__ + '.' + obj.id
        working_objects[new_key] = obj.to_dict()
        self.objects = working_objects

    def save(self):
        '''serializes __objects to the JSON file (path: __file_path)

        '''
        with open(self.file_path, "w") as new_file:
            json.dump(self.objects, new_file)

    def reload(self):
        '''deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists)

        '''
        if path.exists(self.file_path):
            with open(self.file_path, "r") as loading_file:
                self.objects = json.load(loading_file)

    @property
    def objects(self):
        '''Getter for __objects

        '''
        return self.__objects

    @objects.setter
    def objects(self, new_objects):
        '''Setter for __objects

        '''
        if type(new_objects) is not dict:
            raise TypeError("New objects must be a dict")
        self.__objects = new_objects

    @property
    def file_path(self):
        '''Getter for __file_path

        '''
        return self.__file_path

    @file_path.setter
    def file_path(self, new_path):
        '''Setter for __file_path

        Args:
            new_path: new path to assign to __file_path
        '''
        if type(new_path) is not str:
            raise TypeError("The new path must be a string")
        self.__file_path = new_path

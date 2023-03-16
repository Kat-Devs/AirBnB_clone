#!/bin/usr/python3
'''
    models.engine.file_storage.py: Class to
    serialize and deserialize data
'''

import json
import os
from datetime import datetime
from models.base_model import BaseModel


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        ''' Returns the dictionary __objects'''
        return self.__objects
    
    def new(self, obj):
        ''' Sets in __objects the obj with key
        <obj class name>.id '''
        key = f'{type(obj).__name__}.{obj.id}'
        self.__objects[key] = obj

    def save(self):
        ''' Serializes __objects to JSON file
        (path: __file_path)'''
        new_dict = {}
        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(new_dict, f)

    def reload(self):
        '''Deserializes JSON file to __objects'''
        try:
            with open(self.__file_path, mode="r", encoding="utf-8") as f:
                obj_dict = json.load(f)
                for key, value in obj_dict.items():
                    cls_name, obj_id = key.split('.')
                    obj_dict[key]['created_at'] = datetime.strptime(obj_dict[key]['created_at'], 
                    '%Y-%m-%dT%H:%M:%S.%f')
                    obj_dict[key]['updated_at'] = datetime.datetime.strptime(obj_dict[key]['updated_at'],
                    '%Y-%m-%dT%H:%M:%S.%f')
                    self.__objects[key] = eval(cls_name)(**obj_dict[key])
        except FileNotFoundError:
            pass


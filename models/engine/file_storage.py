#!/usr/bin/python3
import json
import os
import models

class FileStorage:
    '''
    Serialilzes instances to a JSON file and
    deserializes JSON file to instances
    '''
    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''
        Returns __objects dict
        '''
        return self.__objects

    def new(self, obj):
        '''
        Sets obj with key <obj class name>.id in
        __objects
        '''
        key = f'{obj.__class__.__name__}.{obj.id}'
        self.__objects[key] = obj

    def save(self):
        '''
        Serializes __objects to JSON file
        (path: __File_path)
        '''
        new_dict = {}
        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict()
        with open(self.__file_path, mode="w",encoding="utf-8") as f:
            json.dump(new_dict, f)

    def reload(self):
        '''
        Deserialize JSON file to __objects if file exists
        '''
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r", encoding="utf-8") as f:
                json_data = json.load(f)
                for key, value in json_data.items():
                    cls_name = key.split('.')[0]
                    if cls_name in models.__dict__:
                        cls = models.__dict__[cls_name]
                        instance = cls(**value)
                        self.__objects[key] = instance
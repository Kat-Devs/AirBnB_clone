#!/usr/bin/python3
import json

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
        Deserializes JSON file to __objects
        '''
        try:
            with open(self.__file_path, mode="r",encoding="utf-8") as f:
                new_dict = json.load(f)
                for key, value in new_dict.items():
                    cls_name = key.split('.')[0]
                    obj = eval(cls_name)(**value)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
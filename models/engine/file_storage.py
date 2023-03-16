#!/usr/bin/python3
import json
import os
import models
from models.base_model import BaseModel
from models.user import User

class FileStorage:
    '''
    Serialilzes instances to a JSON file and
    deserializes JSON file to instances
    '''
    __file_path = "file.json"
    __objects = {}
    __classes = {
        "BaseModel": BaseModel, 
        "User": User}

    def all(self, cls=None):
        '''
        Returns __objects dict
        '''
        if cls is None:
            return self.__objects
        
        if isinstance(cls, str):
            cls = self.__classes.get(cls)

        return {k: v for k, v in self.__objects.items() if isinstance(v, cls)}

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
        with open(self.__file_path, mode="w", encoding="utf-8") as f:
            obj_dict = {k: v.to_dict() for k, v in self.__objects.items()}
            json.dump(obj_dict, f)

    def reload(self):
        try:
            with open(self.__file_path, mode="r", encoding="utf-8") as f:
                obj_dict = json.load(f)
                for key, value in obj_dict.items():
                    cls_name = value["__class__"]
                    if cls_name in self.__classes:
                        cls = self.__classes[cls_name]
                        instance = cls(**value)
                        self.__objects[key] = instance
        except FileNotFoundError:
            pass 

    """ def reload(self):
        '''
        Deserialize JSON file to __objects if file exists
        '''
        # Check if JSON file exists
        if os.path.exists(self.__file_path):
            # Open the JSON file and load its contents into __objects
            with open(self.__file_path, "r", encoding="utf-8") as f:
                # Deserialize the JSON data and store it in a temporary variable
                json_data = json.load(f)
                # Loop through the deserialized data and create instances of the
                # corresponding class for each object
                for key, value in json_data.items():
                     # Extract the class name from the key and check if it exists in
                    # the models module's namespace
                    cls_name = key.split('.')[0]
                    if cls_name in models.__dict__:
                         # If the class exists, create an instance of it with the
                        # corresponding data and add it to __objects
                        cls = models.__dict__[cls_name]
                        instance = cls(**value)
                        self.__objects[key] = instance """
import json
import datetime
from models.base_model import BaseModel


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary of objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Adds new object to __objects with key <obj class name>.id
        """
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file at __file_path
        """
        obj_dict = {}
        for key, value in FileStorage.__objects.items():
            obj_dict[key] = value.to_dict()

        with open(FileStorage.__file_path, mode="w", encoding="utf-8") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """
        Deserializes the JSON file at __file_path to __objects
        """
        try:
            with open(FileStorage.__file_path, mode="r", encoding="utf-8") as f:
                obj_dict = json.load(f)
            for key, value in obj_dict.items():
                class_name, obj_id = key.split(".")
                obj_dict[key]["created_at"] = datetime.strptime(obj_dict[key]["created_at"],
                                                                "%Y-%m-%dT%H:%M:%S.%f")
                obj_dict[key]["updated_at"] = datetime.strptime(obj_dict[key]["updated_at"],
                                                                "%Y-%m-%dT%H:%M:%S.%f")
                cls = BaseModel
                if class_name == "BaseModel":
                    cls = BaseModel
                obj = cls(**value)
                FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
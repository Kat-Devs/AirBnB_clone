#!/usr/bin/python3

"""
class BaseModel that defines all common attributes/methods for other classes
"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """Class that will be inherited by all other classes"""

    def __init__(self, *args, **kwargs):
        """Instantiation of base model class"""
        if kwargs:
            for key in kwargs:
                if key == "created_at" or key == "updated_at":
                    kwargs[key] = datetime.strptime(kwargs[key],
                                                    "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, kwargs[key])
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Returns a string representation of the instance"""
        return "[{}] ({}) <{}>".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates the public instance attribute updated_at with the current
        datetime"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__ of the
        instance"""
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict

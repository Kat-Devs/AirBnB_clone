#!/usr/bin/python3

import uuid
import datetime


class BaseModel:
    """
    Base class for other classes to inherit from.

    Attributes:
        id (str): The ID of the instance.
        created_at (datetime): The datetime the instance was created.
        updated_at (datetime): The datetime the instance was last updated.
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the BaseModel class.

        Args:
            *args: Not used.
            **kwargs: A dictionary of attribute names and values to set on the instance.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key != '__class__':
                    setattr(self, key, value)
            self.id = str(kwargs.get('id', uuid.uuid4()))
            self.created_at = kwargs.get('created_at', datetime.datetime.now())
            self.updated_at = datetime.datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()

    def __str__(self):
        """
        Returns a string representation of the instance.

        Returns:
            str: A string representation of the instance.
        """
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the updated_at attribute with the current datetime.
        """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """
        Returns a dictionary representation of the instance.

        Returns:
            dict: A dictionary representation of the instance.
        """
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = type(self).__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict


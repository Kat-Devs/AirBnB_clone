#!/usr/bin/python3

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    '''
    Base class for other models to inherit from.
    Provides common attributes and methods
    '''

    def __init__(self, *args, **kwargs):
        ''' Inits a new instance of BaseModel'''
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        ''' Returns string rep of instance'''
        return f'[{type(self).__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        ''' Update updated_at with current datetime'''
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        ''' Returns dict rep of instance
            Dictionary can be used for serialization/deserialization
        '''

        new_dict = self.__dict__.copy()
        new_dict['__class__'] = type(self).__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.created_at.isoformat()
        return new_dict

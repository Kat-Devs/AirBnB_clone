#!/usr/bin/python3

import uuid
from datetime import datetime


class BaseModel:
    '''
    Base class for other models to inherit from.
    Provides common attributes and methods
    '''

    def __init__(self):
        ''' Inits a new instance of BaseModel'''
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        ''' Returns string rep of instance'''
        return f'[{type(self).__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        ''' Update updated_at with current datetime'''
        self.updated_at = datetime.now()

    def to_dict(self):
        ''' Returns dict rep of instance
            Dictionary can be used for serialization/deserialization
        '''

        new_dict = self.__dict__.copy()
        new_dict['__class__'] = type(self).__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.created_at.isoformat()
        return new_dict

#!/usr/bin/python3

import unittest
from datetime import datetime
from models.base_model import BaseModel
import uuid

class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.model = BaseModel()

    def test_id(self):
        ''' Test whether id is a string'''
        self.assertIsInstance(self.model.id, str)

        '''Test each instance has unique id'''
        other_model = BaseModel()
        self.assertNotEqual(self.model.id, other_model.id)

    def test_created_at(self):
        ''' Check if created_at is a datetime obj'''
        self.assertIsInstance(self.model.created_at, datetime)

    def test_updated_at(self):
        '''' Check if updated_at is a datetime obj'''
        self.assertIsInstance(self.model.updated_at, datetime)

        '''Test save method updates updated_at'''
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(old_updated_at, self.model.updated_at)

    def test_to_dict(self):
        ''' Test that to_dict returns dict'''
        self.assertIsInstance(self.model.to_dict(), dict)

        ''' Test __class__ attribute for correctness'''
        self.assertEqual(self.model.to_dict()['__class__'], 'BaseModel')

        ''' Test that created_at and updated_at attributes are iso format'''
        self.assertIsInstance(self.model.to_dict()['created_at'], str)
        self.assertIsInstance(self.model.to_dict()['updated_at'], str)
        datetime.strptime(self.model.to_dict()['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
        datetime.strptime(self.model.to_dict()['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')

    def test_init_with_dict(self):
        """Test initialization of BaseModel instance from dictionary"""
        bm_dict = {'id': str(uuid.uuid4()),
                   'created_at': datetime.now().isoformat(),
                   'updated_at': datetime.now().isoformat(),
                   '__class__': 'BaseModel'}
        bm = BaseModel(**bm_dict)
        self.assertIsInstance(bm, BaseModel)
        self.assertEqual(bm.id, bm_dict['id'])
        self.assertEqual(bm.created_at, datetime.fromisoformat(bm_dict['created_at']))
        self.assertEqual(bm.updated_at, datetime.fromisoformat(bm_dict['updated_at']))


if __name__ == '__main__':
    unittest.main()
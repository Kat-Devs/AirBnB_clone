#!/usr/bin/python3

import unittest
import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Tests for the BaseModel class."""

    def test_init(self):
        """Test initialization of a new BaseModel instance."""
        b = BaseModel()
        self.assertIsInstance(b, BaseModel)
        self.assertIsInstance(b.id, str)
        self.assertIsInstance(b.created_at, datetime.datetime)
        self.assertIsInstance(b.updated_at, datetime.datetime)

    def test_init_kwargs(self):
        """Test initialization of a new BaseModel instance with kwargs."""
        kwargs = {'id': '1234', 'created_at': '2022-01-01T00:00:00.000000',
              'updated_at': '2022-01-01T00:01:00.000000', 'name': 'test'}
        b = BaseModel(**kwargs)
        self.assertEqual(b.id, kwargs['id'])
        self.assertEqual(b.created_at, datetime.datetime.\
                fromisoformat(kwargs['created_at']))
        self.assertEqual(b.updated_at, datetime.datetime.fromisoformat(kwargs['updated_at']))
        self.assertEqual(b.name, 'test')


    def test_str(self):
        """Test string representation of a BaseModel instance."""
        b = BaseModel()
        s = f"[{type(b).__name__}] ({b.id}) {b.__dict__}"
        self.assertEqual(str(b), s)

    def test_save(self):
        """Test updating of the updated_at attribute."""
        b = BaseModel()
        original_updated_at = b.updated_at
        b.save()
        self.assertNotEqual(b.updated_at, original_updated_at)

    def test_to_dict(self):
        """Test dictionary representation of a BaseModel instance."""
        b = BaseModel()
        d = b.to_dict()
        self.assertIsInstance(d, dict)
        self.assertEqual(d['__class__'], type(b).__name__)
        self.assertEqual(d['id'], b.id)
        self.assertEqual(d['created_at'], b.created_at.isoformat())
        self.assertEqual(d['updated_at'], b.updated_at.isoformat())

if __name__ == '__main__':
    unittest.main()

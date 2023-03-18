import datetime
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class"""

    def setUp(self):
        """Create a new instance of the BaseModel class"""
        self.base_model = BaseModel()

    def test_id(self):
        """Test that the id attribute is a string"""
        self.assertIsInstance(self.base_model.id, str)

    def test_created_at(self):
        """Test that the created_at attribute is a datetime object"""
        self.assertIsInstance(self.base_model.created_at, datetime.datetime)

    def test_updated_at(self):
        """Test that the updated_at attribute is a datetime object"""
        self.assertIsInstance(self.base_model.updated_at, datetime.datetime)

    def test_save(self):
        """Test that the save method updates the updated_at attribute"""
        old_updated_at = self.base_model.updated_at
        self.base_model.save()
        new_updated_at = self.base_model.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

    def test_to_dict(self):
        """Test that the to_dict method returns a dictionary"""
        obj_dict = self.base_model.to_dict()
        self.assertIsInstance(obj_dict, dict)

    def test_to_dict_contains_classname(self):
        """Test that the to_dict method includes the class name"""
        obj_dict = self.base_model.to_dict()
        self.assertIn('__class__', obj_dict)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')

    def test_to_dict_contains_createdat(self):
        """Test that the to_dict method includes the created_at attribute"""
        obj_dict = self.base_model.to_dict()
        self.assertIn('created_at', obj_dict)

    def test_to_dict_contains_updatedat(self):
        """Test that the to_dict method includes the updated_at attribute"""
        obj_dict = self.base_model.to_dict()
        self.assertIn('updated_at', obj_dict)

    def test_to_dict_createdat_type(self):
        """Test that the created_at attribute is a string in ISO format"""
        obj_dict = self.base_model.to_dict()
        self.assertIsInstance(obj_dict['created_at'], str)
        self.assertEqual(datetime.datetime.fromisoformat(obj_dict['created_at']), self.base_model.created_at)

    def test_to_dict_updatedat_type(self):
        """Test that the updated_at attribute is a string in ISO format"""
        obj_dict = self.base_model.to_dict()
        self.assertIsInstance(obj_dict['updated_at'], str)
        self.assertEqual(datetime.datetime.fromisoformat(obj_dict['updated_at']), self.base_model.updated_at)

    def test_to_dict_contains_all_attributes(self):
        """Test that the to_dict method includes all instance attributes"""
        self.base_model.name = 'test'
        self.base_model.number = 123
        obj_dict = self.base_model.to_dict()
        self.assertIn('name', obj_dict)
        self.assertIn('number', obj_dict)
        self.assertEqual(obj_dict['name'], 'test')
        self.assertEqual(obj_dict['number'], 123)


if __name__ == '__main__':
    unittest.main()

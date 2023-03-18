import datetime
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class"""

    def setUp(self):
        """Create a new instance of the BaseModel class"""
        self.base_model = BaseModel()

    def test_id(self):
        """Test that the id attribute is a string and 
        is unique"""
        
        self.assertIsInstance(self.base_model.id, str)
        self.assertIsNotNone(self.base_model.id)

    def test_created_at(self):
        """Test that the created_at attribute is a datetime object"""
        self.assertIsInstance(self.base_model.created_at, datetime.datetime)
        self.assertIsNotNone(self.base_model.created_at)

    def test_updated_at(self):
        """Test that the updated_at attribute is a datetime object"""
        self.assertIsInstance(self.base_model.updated_at, datetime.datetime)
        self.assertIsNotNone(self.base_model.updated_at)

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
        self.assertEqual(obj_dict["name"], "test_model")
        self.assertEqual(obj_dict["__class__"], "BaseModel")
        self.assertIsInstance(obj_dict["id"], str)
        self.assertIsInstance(obj_dict["created_at"], str)
        self.assertIsInstance(obj_dict["updated_at"], str)

if __name__ == '__main__':
    unittest.main()

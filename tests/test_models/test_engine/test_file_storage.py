import os
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Tests for the FileStorage class"""

    def setUp(self):
        """Set up a new FileStorage instance for each test"""
        self.file_path = "test_file.json"
        self.storage = FileStorage()
        self.storage._FileStorage__file_path = self.file_path

    def tearDown(self):
        """Remove the test JSON file if it exists"""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all(self):
        """Test that the all() method returns the __objects dictionary"""
        # Add a new object to __objects
        obj = BaseModel()
        self.storage.new(obj)
        self.assertEqual(self.storage.all(), {"BaseModel.{}".format(obj.id): obj})

    def test_new(self):
        """Test that the new() method adds an object to __objects"""
        obj = BaseModel()
        self.storage.new(obj)
        key = "BaseModel.{}".format(obj.id)
        self.assertEqual(self.storage.all()[key], obj)

    def test_save(self):
        """Test that the save() method saves __objects to the JSON file"""
        # Add a new object to __objects
        obj = BaseModel()
        self.storage.new(obj)

        # Save __objects to the test file
        self.storage.save()

        # Read the test file and verify that the object was saved
        with open(self.file_path, "r") as f:
            data = f.read()
            self.assertIn("BaseModel.{}".format(obj.id), data)

    def test_reload(self):
        """Test that the reload() method loads objects from the JSON file"""
        # Save a new object to the test file
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()

        # Reset __objects and call reload()
        self.storage._FileStorage__objects = {}
        self.storage.reload()

        # Verify that the object was reloaded
        key = "BaseModel.{}".format(obj.id)
        self.assertIn(key, self.storage.all())
        self.assertIsInstance(self.storage.all()[key], BaseModel)

    def test_reload_file_not_found(self):
        """Test that reload() does not raise an exception if the JSON file does not exist"""
        # Remove the test file if it exists
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

        # Call reload() and verify that it does not raise an exception
        try:
            self.storage.reload()
        except Exception as e:
            self.fail("reload() raised an exception: {}".format(e))

if __name__ == '__main__':
    unittest.main()

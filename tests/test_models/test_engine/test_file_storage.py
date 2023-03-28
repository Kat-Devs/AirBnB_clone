import unittest
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.file_path = "test_file.json"
        self.file_storage = FileStorage(self.file_path)
        self.base_model = BaseModel()

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all(self):
        all_objs = self.file_storage.all()
        self.assertIsInstance(all_objs, dict)

    def test_new(self):
        self.file_storage.new(self.base_model)
        self.assertIn("BaseModel." + self.base_model.id, self.file_storage._FileStorage__objects.keys())

    def test_save_reload(self):
        self.file_storage.new(self.base_model)
        self.file_storage.save()
        self.assertTrue(os.path.exists(self.file_path))
        self.file_storage.reload()
        all_objs = self.file_storage.all()
        self.assertIsInstance(all_objs, dict)
        self.assertIn("BaseModel." + self.base_model.id, all_objs.keys())

if __name__ == '__main__':
    unittest.main()

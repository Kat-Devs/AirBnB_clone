#!/usr/bin/python3

'''
Unittests for FileStorage Class
'''
import unittest
import json
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    '''
    TEST CASES FOR FILESTORAGE CLASS
    '''

    def setUp(self):
        '''
        Sets up tests by creating new FileStorage instance
        and deleting the file.json if it exists
        '''
        self.storage = FileStorage
        if os.path.exists("file.json"):
            os.remove("file.json")

    def tearDown(self):
        '''
        Tears down the tests by deleting the file.json
        if it exists
        '''
        if os.path.exists("file.json"):
            os.remove("file.json ")
        
    def test_all(self):
        '''
        Tests all() method by checking type of 
        returned object is dict
        '''
        self.assertIsInstance(self.storage.all(), dict())

    def test_save(self):
        '''
        Tests save() method by creating new BaseModel
        instance, adding it to __objects dict then saving
        it to os. It then loads contents of file into dict
        and verifies BM instance was saved
        '''
        new_model = BaseModel()
        self.storage.new(new_model)
        self.storage.save()
        with open("file.json", "r") as f:
            file_content = json.load(f)
        key = f"{new_model.__class__.__name__}.{new_model.id}"
        self.assertIn(key, file_content)

    
    def test_reload(self):
        ''''
        Tests reload() method by creating new BM instance,
        adding to __objects and saving it to os. A new 
        FileStorage instance is created and reloads 
        data from os and checks BM instance is in 
        __objects of new FS instance
        '''
        new_model = BaseModel()
        self.storage.new(new_model)
        self.storage.save()

        new_storage = FileStorage()
        new_storage.reload()
        key = f'{new_model.__class__.__name__}.{new_model.id}'
        self.assertIn(key, new_storage.all())
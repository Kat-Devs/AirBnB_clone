#!/usr/bin/python3
'''
    models/__init__.py: initializes package modules
'''

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
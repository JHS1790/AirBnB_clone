#!/usr/bin/python3
'''file for enabling storage'''

from .engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
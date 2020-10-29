'''initializer for models module'''

from .engine.file_storage import FileStorage

__all__ = ["BaseModel"]
storage = FileStorage()
storage.reload()
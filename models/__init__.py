'''initializer for models module'''

__all__ = ['BaseModel', 'storage']

from .storage_enabler import storage
from .base_model import BaseModel
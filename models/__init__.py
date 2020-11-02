'''models module'''

__all__ = ['BaseModel', 'User']

from .storage_enabler import storage
from .base_model import BaseModel
from .user import User
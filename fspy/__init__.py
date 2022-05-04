"""Top-level package for Python In Memory FileSystem."""
from .fspy import FileSystem
from .cli import handle_crud
__author__ = """Matthew X Staffelbach"""
__email__ = 'xstaffelbach@gmail.com'
__version__ = '0.1.0'

__all__ = ['FileSystem', 'handle_crud', 'Directory']

'''This file handles system variables and process them to reuse them in the code.'''

import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

LOGGING_LEVEL = os.environ.get('LOGGING_LEVEL', 'INFO')

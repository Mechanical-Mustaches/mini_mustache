'''
use this document to create new buttons on the shuffleboard

'''
from robot import *

# fill in this dictionary with names and functions to add to webpage

print('IMPORTING STACHEBOARD')

buttons = {
    'test1': lambda: print('test1'),
    'test2': lambda: print('test2'),
    'nemo.sleep()': lambda: nemo.sleep(),
    'nemo.rainbow()': lambda: nemo.rainbow()
}

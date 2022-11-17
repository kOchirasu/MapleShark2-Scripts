''' DARK_STREAM '''
from script_api import *
from item import *

f = add_byte("Function")
if f == 0:
    pass # Open Dialog
elif f == 1:
    add_int("Score")
elif f == 2:
    add_int("unknown")
    add_int("unknown")
    add_int("unknown")
    add_int("unknown")
    add_int("unknown")
    count = add_byte("count")
    for i in range(count):
        decode_item_entity()

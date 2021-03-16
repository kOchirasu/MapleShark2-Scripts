from script_api import *

f = add_byte("function")
if f == 0:
    pass
elif f == 1:
    add_int("Unknown")
elif f == 2:
    add_int("Unknown")
elif f == 3:
    add_byte("Unknown")
    add_int("Unknown")
    add_int("Unknown")
    add_int("Unknown")
"""for i in range(15):
    with Node("Entry " + str(i), True):
        add_int("Id")
        add_int("Level")
        add_int("Unknown")
        add_short("Unknown")
        add_field("Unknown", 38)
"""

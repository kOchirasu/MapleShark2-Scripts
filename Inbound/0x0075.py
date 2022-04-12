''' LIFTABLE '''
from script_api import *

def decode_liftable(): # CLiftableObject
    add_str("Unknown")
    add_int("Unknown")
    add_unicode_str("Unknown")
    add_unicode_str("Unknown")
    add_unicode_str("Unknown")
    add_unicode_str("Unknown")
    add_bool("Unknown")


f = add_byte("Function")
if f == 0:
    count = add_int("count")
    for i in range(count):
        with Node("Liftable " + str(i), True):
            add_str("Unknown")
            add_byte("Unknown")
            add_int("Unknown")
            add_byte("Unknown")
            add_unicode_str("Unknown")
            add_unicode_str("Unknown")
            add_unicode_str("Unknown")
            add_unicode_str("Unknown")
            add_bool("Unknown")
elif f == 2:
    add_str("Unknown")
    add_byte("Unknown")
    add_int("Unknown")
    add_byte("Unknown")
elif f == 3:
    decode_liftable()
elif f == 4:
    add_str("Unknown")

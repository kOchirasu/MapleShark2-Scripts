from script_api import *

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
    add_str("Unknown")
    add_int("Unknown")
    add_unicode_str("Unknown")
    add_unicode_str("Unknown")
    add_unicode_str("Unknown")
    add_unicode_str("Unknown")
    add_bool("Unknown")
elif f == 4:
    add_str("Unknown")

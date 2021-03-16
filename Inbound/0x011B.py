from script_api import *

f = add_byte("Function")
if f == 22:
    add_int("Unknown")
    add_int("Unknown")
    add_long("Unknown")
    add_unicode_str("UnknownStr")
    add_int("Unknown")
    add_int("Unknown")
    add_int("Unknown")
    add_int("Unknown")
    add_int("Unknown")
    add_int("Unknown")
    add_int("Unknown")
elif f == 23:
    add_long("Unknown")
    add_int("Unknown")
    add_byte("Unknown")
    add_long("Unknown")
    add_int("Unknown")
    add_int("Unknown")
    add_int("Unknown")
    add_long("Unknown")
elif f == 30:
    count = add_byte("Count")
    for i in range(count):
        add_int("Unknown")
        count2 = add_int("Count")
        for j in range(count2):
            add_int("Unknown")
            add_long("Unknown")

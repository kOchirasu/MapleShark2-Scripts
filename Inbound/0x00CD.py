from script_api import *

f = add_byte("Function")
b = add_bool("Unknown")

count = add_int("count")
for i in range(count):
    with Node("Entry " + str(i)):
        add_int("a")
        add_int("a")
        add_unicode_str("a")
        add_long("Timestamp")

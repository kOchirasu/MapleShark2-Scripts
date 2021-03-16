from script_api import *

count = add_int("count")
for i in range(count):
    with Node("Entry " + str(i)):
        add_int("Unknown")
        add_int("Unknown")

add_byte("Unknown")

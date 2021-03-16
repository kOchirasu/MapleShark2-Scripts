from script_api import *

f = add_byte("Function")

if f == 0:
    count = add_int("count")
    for i in range(count):
        add_int("Unknown")
    add_long("Unknown")
    add_int("Unknown")
elif f == 1:
    add_int("Unknown")

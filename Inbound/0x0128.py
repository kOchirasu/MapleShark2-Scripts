from script_api import *

f = add_byte("Function")

if f == 0:
    count = add_short("Count")
    for i in range(count):
        add_int("StampId")
    count = add_short("Count")
    for i in range(count):
        add_int("Unknown")
        add_int("-1")
        add_int("217538647")

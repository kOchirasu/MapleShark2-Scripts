from script_api import *

f = add_byte("Function")
if f == 0:
    for i in range(8):
        add_short("Unknown")
elif f == 1:
    count = add_short("Count")
    for i in range(count):
        add_short("Unknown")

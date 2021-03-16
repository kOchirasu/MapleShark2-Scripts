from script_api import *

f = add_byte("function")
if f == 0:
    add_byte("Unknown")
    add_int("ServerTick")
    add_int("Duration (ms)")
    add_int("Unknown")
elif f == 1:
    add_int("Unknown")
    add_int("Unknown")
    add_int("Unknown")
    add_int("Unknown")
elif f == 2:
    add_byte("Unknown")
    add_int("Unknown")
    add_int("Unknown")
    add_int("Unknown")
elif f == 3:
    pass # none
elif f == 4:
    pass # none
elif f == 5:
    pass # none

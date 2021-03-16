from script_api import *

f = add_byte("function")
if f == 0:
    add_int("ServerTick")
    add_long("Timestamp")
    add_byte("Unknown")
    add_int("Unknown")
    add_int("Key")
elif f == 1:
    add_int("ServerTick")
    add_long("Timestamp")
    add_byte("Unknown")
    add_int("Unknown")
elif f == 2:
    add_int("ServerTick")
    add_long("Timestamp")
    add_byte("Unknown")
    add_int("Unknown")
elif f == 3:
    add_long("Timestamp")

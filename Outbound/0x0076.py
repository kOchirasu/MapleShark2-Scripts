from script_api import *

f = add_byte("function")
if f == 0:
    add_long("ItemUid")
    add_field("Unknown", 8)
    b = add_bool("UseLock")
    if b:
        add_byte("Unknown")
        add_short("LockedIndex")
elif f == 2: # Select new option
    add_long("ItemUid")

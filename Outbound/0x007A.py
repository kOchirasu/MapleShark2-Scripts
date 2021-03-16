from script_api import *

f = add_byte("Function")
if f == 0: # Store item
    add_long("ItemUid")
    add_short("Slot")
    add_int("Amount")
elif f == 3: # Move item
    add_long("ItemUid")
    add_short("Slot")
elif f == 7:
    # load inventory
    pass

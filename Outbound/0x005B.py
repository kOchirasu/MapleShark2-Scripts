from script_api import *

f = add_byte("function")

if f == 0: # open/close ui
    add_bool("IsOpen")
elif f == 1: # add item
    add_int("Unknown") # -1
    add_long("ItemUid")
    add_int("Amount")
elif f == 2: # remove item
    add_long("ItemUid")
elif f == 3: # confirm dismantle
    pass # none

from script_api import *

f = add_byte("function")

if f == 0:
    pass # opening ui
elif f == 1: # add item to ui
    add_bool("0 - lock|1 - unlock")
    add_long("ItemUid")
elif f == 2: # remove item from ui
    add_long("ItemUid")
elif f == 3:
    add_bool("0 - lock|1 - unlock")

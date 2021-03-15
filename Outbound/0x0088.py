from script_api import *

f = AddByte("function")

if f == 0:
    pass # opening ui
elif f == 1: # add item to ui
    AddBool("0 - lock|1 - unlock")
    AddLong("ItemUid")
elif f == 2: # remove item from ui
    AddLong("ItemUid")
elif f == 3:
    AddBool("0 - lock|1 - unlock")

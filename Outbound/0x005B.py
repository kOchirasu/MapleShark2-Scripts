from script_api import *

f = AddByte("function")

if f == 0: # open/close ui
    AddBool("IsOpen")
elif f == 1: # add item
    AddInt("Unknown") # -1
    AddLong("ItemUid")
    AddInt("Amount")
elif f == 2: # remove item
    AddLong("ItemUid")
elif f == 3: # confirm dismantle
    pass # none

from script_api import *

f = AddByte("Function")
if f == 0: # Start fishing
    AddLong("RodItemUid")
elif f == 9:
    AddInt("Unknown")
elif f == 8: # Success
    AddBool("Auto") #  0 = manual, 1 = auto
elif f == 10: # Failed
    pass

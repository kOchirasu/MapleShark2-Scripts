from script_api import *

f = add_byte("Function")
if f == 0: # Start fishing
    add_long("RodItemUid")
elif f == 9:
    add_int("Unknown")
elif f == 8: # Success
    add_bool("Auto") #  0 = manual, 1 = auto
elif f == 10: # Failed
    pass

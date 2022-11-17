''' CHANGE_ATTRIBUTES_SCROLL '''
from script_api import *

f = add_byte("Function")
if f == 1: # change attributes
    add_long("ScrollUid")
    add_long("EquipUid")
    add_long("unknown")
    add_byte("unknown")
    b = add_bool("useLock")
    if b:
        add_byte("IsSpecialAttribute")
        add_short("attribute")
elif f == 3: # select new
    add_long("EquipUid")

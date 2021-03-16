from script_api import *

f = add_byte("Function")

if f == 1: # use scroll
    add_long("ScrollUid")
    add_long("EquipUid")
    add_field("Unknown 9", 9)
    b = add_bool("UseLock")
    if b:
        add_byte()
        add_short()
elif f == 3: # select new
    add_long("EquipUid")

from script_api import *
from item import *

f = add_byte("Function")

if f == 0: # use scroll response
    add_long("ScrollUid")
elif f == 2: # use scroll on item
    add_long("EquipUid")
    decode_item(0)
elif f == 3: # select new item
    add_long("EquipUid")
    decode_item(0)

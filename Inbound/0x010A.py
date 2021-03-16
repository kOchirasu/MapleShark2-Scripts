from script_api import *

f = add_byte("function")
if f == 0: # create pet badge
    add_long("PetItemUid")
    add_long("BadgeItemUid")
    add_int("PetItemId")

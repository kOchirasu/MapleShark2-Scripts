from script_api import *

f = AddByte("function")
if f == 0: # create pet badge
    AddLong("PetItemUid")
    AddLong("BadgeItemUid")
    AddInt("PetItemId")

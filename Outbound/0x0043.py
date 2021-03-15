from script_api import *

f = AddByte("function")
if f == 2: # put on item
    AddLong("ItemUid")
    AddLong("AccountUid")
    AddUnicodeString("Slot")
elif f == 3: # swap outfits
    AddLong("DollUid")
elif f == 7: # remove item
    AddLong("ItemUid")
    AddUnicodeString("Slot")
elif f == 10: # remove doll
    AddLong("DollUid")

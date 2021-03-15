from script_api import *
from common import *

f = AddByte("Function")
if f == 2: # opening furnishing box
    AddInt("storage count")
elif f == 3:
    id = AddInt("ItemId")
    AddLong("ItemUid")
    AddByte("rarity")
    AddInt("Index")
    DecodeItem(id)
elif f == 4:
    AddLong("ItemUid")
elif f == 5: # opening furnishing box
    AddLong("ItemUid")
    AddInt("Count")
elif f == 7: # opening furnishing box
    AddLong("ItemUid")
    AddInt("Count")

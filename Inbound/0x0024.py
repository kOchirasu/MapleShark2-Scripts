from script_api import *
from common import *

count = AddByte("function")
if count == 0 or count == 4:
    # 0 == Start List
    # 4 == End List
    pass
elif count == 1:
    AddInt("ItemId")
    AddLong("ItemUid")
    AddLong("Unknown")
    b = AddBool("IsTemplate")
    if b:
        DecodeUgcData()

elif count == 2: # Remove
    AddLong("ItemUid")
elif count == 3: # Update?
    AddLong("ItemUid")
    AddInt("Count")

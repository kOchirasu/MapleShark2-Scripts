from script_api import *
from common import *

f = AddByte("function")

if f == 1: # add item to ui
    AddLong("ItemUid")
    AddShort("slot")
elif f == 2: # remove item from ui
    AddLong("ItemUid")
elif f == 3:
    count = AddByte("count")
    for i in range(count):
        AddLong("ItemUid")
        DecodeItem(0)
elif f == 4:
    AddInt("ErrorCode")

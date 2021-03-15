from script_api import *
from common import *

f = AddByte("function")
if f == 1:
    AddLong("ItemUid")
    DecodeItem(0)
elif f == 2:
    AddLong("ItemUid")
    DecodeItem(0)
elif f == 4:
    AddByte("Unknown")
    AddInt("Unknown")

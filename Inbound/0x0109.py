from script_api import *
from common import *

f = AddByte("function")
if f == 0:
    AddLong("ItemUid")
    AddLong("CreatedItemUid")
    AddShort("Unknown")
    DecodeEquipColor()
    AddInt("EquipColorUnknown")

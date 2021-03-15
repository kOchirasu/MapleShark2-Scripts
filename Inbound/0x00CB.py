from script_api import *
from common import *

f = AddByte("Function")

if f == 0: # use scroll response
    AddLong("ScrollUid")
elif f == 2: # use scroll on item
    AddLong("EquipUid")
    DecodeItem(0)
elif f == 3: # select new item
    AddLong("EquipUid")
    DecodeItem(0)

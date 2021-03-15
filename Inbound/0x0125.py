from script_api import *

f = AddByte("function")

if f == 5:
    AddInt("TabIndex")
    AddInt("Type") # 0=Equip, 1=Outfit
    AddInt("HotKey")
    AddUnicodeString("Name")
    count = AddInt("count")
    for i in range(count):
        with Node("Equip " + str(i), True):
            AddLong("ItemUid")
            AddInt("ItemId")
            AddInt("Slot") # Not sure what slot this is
            AddInt("Rarity")

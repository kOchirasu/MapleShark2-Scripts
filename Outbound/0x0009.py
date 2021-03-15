from script_api import *
from common import *

f = AddByte("function")

if f == 0:
    AddLong("CharacterId")
    AddShort("Unknown") # 01 00
elif f == 1:
    AddByte("Gender")
    AddShort("JobCode")
    AddUnicodeString("Name")
    DecodeSkinColor()
    AddField("Unknown", 2)
    count = AddByte("count")
    for i in range(count):
        id = AddInt("ItemId")
        AddUnicodeString("EquipSlot")
        DecodeEquipColor()
        AddInt("AppearanceFlag")
        # Item positioning
        if id / 100000 == 113:
            AddField("Cap Position", 13 * 4)
        elif id / 100000 == 102:
            AddField("Back Hair Position", 4 * 7)
            AddField("Front Hair Position", 4 * 7)
        elif id / 100000 == 104:
            AddField("Cosmetic Position", 4 * 4)
    AddInt("Unknown")
elif f == 2: # delete
    AddLong("CharacterId")
elif f == 3: # cancel delete
    AddLong("CharacterId")

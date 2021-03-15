from script_api import *

def DecodeKeyBinds():
    count = AddInt("KeyBindCount")
    for i in range(count):
        with Node("Key " + str(i)):
            AddInt("KeyCode")
            AddInt("Type")
            AddLong("uid")
            AddInt("Unknown")
            AddByte("Priority")

def DecodeHotbars():
    AddShort("ActiveHotbar")
    hotbarCount = AddShort("HotbarCount")
    for i in range(hotbarCount):
        with Node("HotBar " + str(i), True):
            quickslotCount = AddInt("QuickSlotCount")
            for j in range(quickslotCount):
                with Node("QuickSlot " + str(j)):
                    AddInt("SlotId")
                    AddInt("SkillId")
                    AddInt("ItemId")
                    AddLong("ItemUid")

f = AddByte("Function")
if f == 2:
    DecodeKeyBinds()
elif f == 3 or f == 4:
    AddShort("HotbarId")
    AddInt("SkillId")
    AddInt("ItemId")
    AddLong("ItemUid")
    AddInt("TargetSlot")
elif f == 5:
    AddShort("HotbarId")
    AddInt("SkillId")
    AddLong("ItemUid")
elif f == 7:
    DecodeHotbars()
elif f == 8:
    AddShort("HotbarId")

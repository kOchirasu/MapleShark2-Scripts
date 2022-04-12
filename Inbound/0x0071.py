''' KEY_TABLE '''
from script_api import *

def decode_key_binds():
    count = add_int("KeyBindCount")
    for i in range(count):
        with Node("Key " + str(i)):
            add_int("KeyCode")
            add_int("Type")
            add_long("uid")
            add_int("Unknown")
            add_byte("Priority")

def decode_hotbars():
    add_short("ActiveHotbar")
    hotbarCount = add_short("HotbarCount")
    for i in range(hotbarCount):
        with Node("HotBar " + str(i), True):
            quickslotCount = add_int("QuickSlotCount")
            for j in range(quickslotCount):
                with Node("QuickSlot " + str(j)):
                    add_int("SlotId")
                    add_int("SkillId")
                    add_int("ItemId")
                    add_long("ItemUid")


f = add_byte("Function")
if f == 0: # Keyboard
    isDefault = add_byte("IsDefault")
    if isDefault == 1:
        pass # ./Data/Xml/Table/default/DefaultKey.xml
    else:
        decode_key_binds()
        decode_hotbars()
elif f == 7:
    decode_hotbars()
elif f == 9: # AskKeyboardOrMouse
    pass

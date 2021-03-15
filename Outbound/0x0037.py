from script_api import *
from common import *

def DecodeCubeItemInfo():
    with Node("CubeItemInfo"):
        AddInt("ItemId")
        AddLong("ItemUid")
        AddLong("Unknown")
        b = AddBool("IsUgc")
        if b:
            DecodeUgcData()


f = AddByte("function")
if f == 1: # hold cube
    DecodeCubeItemInfo()
elif f == 2: # buy plot
    AddInt("PlotId")
    AddInt("Unknown")
elif f == 6: # forfeit plot
    pass # none
elif f == 9: # extend plot?
    pass # none
elif f == 10: # place cube
    AddFloat("CoordB")
    DecodeCubeItemInfo()
    AddInt("Rotation")
elif f == 12: # request remove cube
    AddFloat("CoordB")
elif f == 14: # rotate furnishing
    AddFloat("CoordB")
    AddBool("Rotate?")
elif f == 15: # replace cube
    AddFloat("CoordB")
    DecodeCubeItemInfo()
    AddInt("Rotation")
elif f == 17: # pick up object
    AddInt("CoordB")
elif f == 18: # throw object
    pass # ??
elif f == 21: # set home name
    AddUnicodeString("HomeName")
elif f == 23:
    AddInt("Unknown")
elif f == 24: # set password
    AddBool("HasPassword")
    AddUnicodeString("Password")
elif f == 25: # thumbs up house
    pass # none
elif f == 29: # set home message
    AddUnicodeString("Message")
elif f == 31: # clear home cubes
    pass # none
elif f == 35: # load save?
    AddInt("slot")
elif f == 37: # increase area
    pass # none
elif f == 38: # decrease area
    pass # none
elif f == 40: # design rank reward
    pass # none
elif f == 42: # set permission 1
    AddByte("PermissionType")
    AddByte("PermissionSetting")
elif f == 43: # set permission 2
    AddByte("PermissionType")
    AddByte("PermissionSetting")
elif f == 44: # increase height
    pass # none
elif f == 45: # decrease height
    pass # none
elif f == 46: # save house
    AddInt("Slot")
    AddUnicodeString("SaveName")
elif f == 48: # confirm load save
    AddInt("slot")
elif f == 49: # kick from house
    pass # none
elif f == 51: # change background
    AddByte("Index")
elif f == 52: # change lighting
    AddByte("Index")
elif f == 54: # change camera
    AddByte("Index")
elif f == 64: # save blueprint
    AddInt("Slot")
    AddUnicodeString("SaveName")
elif f == 65: # load blueprint
    AddInt("Slot")
# 0x28 (40) = House Decoration Reward
# Send item inventory, response cube
# 27 B2 79 72 04 3E 95 3C 26 4A E2 8C 5E 00 00 00 00 09 00 00 00 00 00 00 00 B0 04 00 00 00 00 00 00 02 00 00 00 06 00 00 00 07 00 00 00

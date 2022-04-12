from script_api import *
from common import *


f = add_byte("function")
if f == 1: # hold cube
    decode_cube_item_info()
elif f == 2: # buy plot
    add_int("PlotId")
    add_int("Unknown")
elif f == 6: # forfeit plot
    pass # none
elif f == 9: # extend plot?
    pass # none
elif f == 10: # place cube
    add_float("CoordB")
    decode_cube_item_info()
    add_int("Rotation")
elif f == 12: # request remove cube
    add_float("CoordB")
elif f == 14: # rotate furnishing
    add_float("CoordB")
    add_bool("Rotate?")
elif f == 15: # replace cube
    add_float("CoordB")
    decode_cube_item_info()
    add_int("Rotation")
elif f == 17: # pick up object
    add_int("CoordB")
elif f == 18: # throw object
    pass # ??
elif f == 21: # set home name
    add_unicode_str("HomeName")
elif f == 23:
    add_int("Unknown")
elif f == 24: # set password
    add_bool("HasPassword")
    add_unicode_str("Password")
elif f == 25: # thumbs up house
    pass # none
elif f == 29: # set home message
    add_unicode_str("Message")
elif f == 31: # clear home cubes
    pass # none
elif f == 35: # load save?
    add_int("slot")
elif f == 37: # increase area
    pass # none
elif f == 38: # decrease area
    pass # none
elif f == 40: # design rank reward
    pass # none
elif f == 42: # set permission 1
    add_byte("PermissionType")
    add_byte("PermissionSetting")
elif f == 43: # set permission 2
    add_byte("PermissionType")
    add_byte("PermissionSetting")
elif f == 44: # increase height
    pass # none
elif f == 45: # decrease height
    pass # none
elif f == 46: # save house
    add_int("Slot")
    add_unicode_str("SaveName")
elif f == 48: # confirm load save
    add_int("slot")
elif f == 49: # kick from house
    pass # none
elif f == 51: # change background
    add_byte("Index")
elif f == 52: # change lighting
    add_byte("Index")
elif f == 54: # change camera
    add_byte("Index")
elif f == 64: # save blueprint
    add_int("Slot")
    add_unicode_str("SaveName")
elif f == 65: # load blueprint
    add_int("Slot")
# 0x28 (40) = House Decoration Reward
# Send item inventory, response cube
# 27 B2 79 72 04 3E 95 3C 26 4A E2 8C 5E 00 00 00 00 09 00 00 00 00 00 00 00 B0 04 00 00 00 00 00 00 02 00 00 00 06 00 00 00 07 00 00 00

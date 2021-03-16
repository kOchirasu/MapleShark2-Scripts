from script_api import *
from common import *

f = add_byte("function")

# socket Transfer
if f == 13: # 0x0D
#case 16: # 0x10
    pass
# Manage
elif f == 9: # put on gem
    add_long("EquipUid")
    #add_long("GemstoneUid") # This uid here becomes changed from actual gem uid
    add_byte("SocketSlot")
    b = add_bool("flag")
    if b:
        decode_gemstone()
elif f == 11: # 0x0B remove gem
    add_long("EquipUid")
    add_byte("SocketSlot")
#case 18: # 0x12
# Upgrade
elif f == 5: # upgrade gem
    add_long("ItemUid")
    add_byte("Unknown")
    add_bool("Unknown") # 1
    add_byte("rarity?") # 4
    add_long("GemstoneUid")
    b = add_bool("Success")
    if b:
        decode_gemstone()
elif f == 7: # response put gem in upgrade ui
    add_long("EquipUid") # If gemstone is on an equip, else: 0
    add_byte("Equipped") # 255 = not equipped, 1 = equipped?
    add_long("GemstoneUid")
    add_float("SuccessRate")
#case 18: # 0x12
# socket unlock
elif f == 1:
    b = add_bool("Unknown")
    add_long("Unknown")
    if b:
        add_byte("Unknown")
        decode_gem_sockets()
        b = add_bool("Unknown")
        if b:
            pass
elif f == 3: # response put acc in unlock socket ui
    add_long("Unknown")
    add_byte("Unknown") # FF
    add_long("EquipUid")
    add_float("SuccessRate")

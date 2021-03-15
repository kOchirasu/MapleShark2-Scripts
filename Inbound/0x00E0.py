from script_api import *
from common import *

f = AddByte("function")

# socket Transfer
if f == 13: # 0x0D
#case 16: # 0x10
    pass
# Manage
elif f == 9: # put on gem
    AddLong("EquipUid")
    #AddLong("GemstoneUid") # This uid here becomes changed from actual gem uid
    AddByte("SocketSlot")
    b = AddBool("flag")
    if b:
        DecodeGemstone()
elif f == 11: # 0x0B remove gem
    AddLong("EquipUid")
    AddByte("SocketSlot")
#case 18: # 0x12
# Upgrade
elif f == 5: # upgrade gem
    AddLong("ItemUid")
    AddByte("Unknown")
    AddBool("Unknown") # 1
    AddByte("rarity?") # 4
    AddLong("GemstoneUid")
    b = AddBool("Success")
    if b:
        DecodeGemstone()
elif f == 7: # response put gem in upgrade ui
    AddLong("EquipUid") # If gemstone is on an equip, else: 0
    AddByte("Equipped") # 255 = not equipped, 1 = equipped?
    AddLong("GemstoneUid")
    AddFloat("SuccessRate")
#case 18: # 0x12
# socket unlock
elif f == 1:
    b = AddBool("Unknown")
    AddLong("Unknown")
    if b:
        AddByte("Unknown")
        DecodeGemSockets()
        b = AddBool("Unknown")
        if b:
            pass
elif f == 3: # response put acc in unlock socket ui
    AddLong("Unknown")
    AddByte("Unknown") # FF
    AddLong("EquipUid")
    AddFloat("SuccessRate")

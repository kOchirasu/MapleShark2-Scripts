from script_api import *

f = AddByte("function")

if f == 0: # EE 4C 75 5B 00 00 00 00 02 46 4E 75 5B 00 00 00 00 4F 4F 75 5B 00 00 00 00
    AddLong("ItemUid")
    count = AddByte("count")
    for i in range(count):
        AddLong("FodderItemUid")
elif f == 2: # put accessory into unlock socket ui
    AddLong("Unknown")
    AddByte("Unknown") # FF
    AddLong("EquipUid")
elif f == 4: # Upgrade gem
    AddLong("EquipUid") # If gemstone is on an equip, else: 0
    AddByte("Unknown")
    AddLong("GemstoneUid")
elif f == 6: # Put gem in upgrade ui
    AddLong("EquipUid") # If gemstone is on an equip, else: 0
    AddByte("Equipped") # 255 = not equipped, 1 = equipped?
    AddLong("GemstoneUid")
elif f == 8: # put gem on equip
    AddLong("EquipUid")
    AddLong("GemstoneUid")
    AddByte("SocketSlot")
elif f == 10: # remove gem
    AddLong("EquipUid")
    AddByte("SocketSlot")

from script_api import *

f = AddByte("Function")
if f == 0:
    # Start enchanting?
    pass
elif f == 1: # Put item enchant
    enchantType = AddByte("EnchantType") # 1 = Ophelia, 2 = Peachy
    AddLong("ItemUid")
    # Response
    # 05 01 00 78 F7 4F 88 84 98 CB 27 02 00 00 00 00 65 00 00 00 1D 00 00 00 00 00 00 00 64 00 00 00 01 00 00 00 00 00 01 00 00 00 14 00 00 00 00 00 6F 12 83 3C 00 00 C8 42 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00
    # 05 02 00 78 F7 4F 88 84 98 CB 27 02 00 00 00 00 65 00 00 00 1D 00 00 00 00 00 00 00 64 00 00 00 01 00 00 00 00 00 01 00 00 00 14 00 00 00 00 00 6F 12 83 3C 00 00 00 00 00 00 00 00 00 00
elif f == 4: # Ophelia Enchant
    AddLong("ItemUid")
    AddField("Unknown", 8)
elif f == 6:
    AddLong("ItemUid") # Peachy enchant

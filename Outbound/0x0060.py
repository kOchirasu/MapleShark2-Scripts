from script_api import *

f = AddByte("function")

if f == 1: # open market
    pass # none
elif f == 2: # list item
    AddLong("ItemUid")
    AddLong("CostPerItem")
    AddInt("Amount")
elif f == 3: # remove listing
    AddLong("ListingUid")
elif f == 4: # search market
    AddInt("Type?")
    AddInt("SubType?")
    AddInt("MinLevel")
    AddInt("MaxLevel")
    AddInt("Job")
    AddInt("MinRarity")
    AddInt("MinEnchant")
    AddInt("MaxEnchant")
    AddByte("MinSocket")
    AddByte("MaxSocket")
    AddUnicodeString("Search Term")
    AddInt("Unknown")
    AddByte("OrderBy") # Level(11 asc, 12 desc),Price(21 asc, 22 desc)
    AddByte("Unknown")
    AddInt("Unknown")
    AddInt("Unknown")
    AddByte("Unknown") # Has bonus attributes
    AddByte("Unknown") # 1?
    for i in range(3):
        AddInt("BonusAttrType")
        AddInt("BonusAttrValue")
elif f == 5: # buy item
    AddLong("ListingUid")
    AddInt("Amount")
elif f == 8: # stage list item
    AddInt("ItemId")
    AddInt("Rarity")

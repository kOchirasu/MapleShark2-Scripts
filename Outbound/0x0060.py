from script_api import *

f = add_byte("function")

if f == 1: # open market
    pass # none
elif f == 2: # list item
    add_long("ItemUid")
    add_long("CostPerItem")
    add_int("Amount")
elif f == 3: # remove listing
    add_long("ListingUid")
elif f == 4: # search market
    add_int("Type?")
    add_int("SubType?")
    add_int("MinLevel")
    add_int("MaxLevel")
    add_int("Job")
    add_int("MinRarity")
    add_int("MinEnchant")
    add_int("MaxEnchant")
    add_byte("MinSocket")
    add_byte("MaxSocket")
    add_unicode_str("Search Term")
    add_int("Unknown")
    add_byte("OrderBy") # Level(11 asc, 12 desc),Price(21 asc, 22 desc)
    add_byte("Unknown")
    add_int("Unknown")
    add_int("Unknown")
    add_byte("Unknown") # Has bonus attributes
    add_byte("Unknown") # 1?
    for i in range(3):
        add_int("BonusAttrType")
        add_int("BonusAttrValue")
elif f == 5: # buy item
    add_long("ListingUid")
    add_int("Amount")
elif f == 8: # stage list item
    add_int("ItemId")
    add_int("Rarity")

from script_api import *

f = add_byte("function")

if f == 5:
    add_int("TabIndex")
    add_int("Type") # 0=Equip, 1=Outfit
    add_int("HotKey")
    add_unicode_str("Name")
    count = add_int("count")
    for i in range(count):
        with Node("Equip " + str(i), True):
            add_long("ItemUid")
            add_int("ItemId")
            add_int("Slot") # Not sure what slot this is
            add_int("Rarity")

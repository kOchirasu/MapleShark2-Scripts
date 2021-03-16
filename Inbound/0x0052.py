from script_api import *
from common import *

# 05 6E 9F D4 DB 71 98 CB 27 87 00 00 00 [f] [uid] [amount] (sell item)
# 03 01 00 00 00 [f] [index] (rebuy)
f = add_byte("function")

if f == 0: # Start load shop
    add_int("NpcId")
    add_int("ShopId")
    add_long("ResetTime")
    add_int("Unknown")
    add_short("ItemCount")
    add_int("Unknown+31") # 5
    add_byte("Unknown+35")
    add_bool("Unknown+36")
    canRestock = add_bool("CanRestock") # button for restocking
    add_bool("Unknown+38")
    add_byte("Unknown+39")
    add_bool("Unknown+40")
    add_bool("Unknown+41")
    add_bool("Unknown+42")
    add_bool("Unknown+43")
    add_str("shop name")
    if canRestock:
        add_byte("Unknown+46")
        add_byte("Unknown+47")
        add_int("Unknown+48")
        add_int("InstantRestockCost")
        add_bool("Unknown+56")
        add_int("Unknown+57")
        add_byte("Unknown+61!") # important
        add_bool("Unknown+62")
        add_bool("Unknown+63")
elif f == 1: # add shop item
    count = add_byte("count")
    for i in range(count):
        with Node("Item " + str(i), i == 0):
            add_int("ShopItemId")
            id = add_int("ItemId")
            add_byte("Unknown") # 1
            add_int("CurrencyId")
            add_int("Unknown") # 0
            add_long("Price")
            #add_int("Unknown")
            add_byte("Rarity")
            add_int("random num")
            add_int("MaxStock?") # 0 = infinite
            add_int("TotalSold")
            add_int("Unknown")
            add_str("ShopCategory")
            add_int("AchievmentRequired")
            add_int("Unknown")
            add_byte("Unknown")
            add_short("Unkown")
            add_byte("Unknown")
            add_short("Unkown")
            add_bool("Unknown")
            add_short("Unkown") # 1
            add_byte("Unkown") # 1
            add_byte("Unkown") # 1 (Has currency id str?)
            add_str("CurrencyIdStr")
            add_short("Unkown")
            add_int("Unknown")
            add_bool("Unknown")
            b = add_bool("Unknown")
            if b:
                pass

            """add_byte("Unknown")
            add_byte("Unknown")
            b = add_bool("Unknown")
            if b:
                b = add_bool("Unknown")
                if b:
                    add_long("Unknown")
                    add_long("Unknown")
                b = add_bool("Unknown")
                if b:
                    count = add_byte("count")
                    for i in range(count):
                        add_int("Unknown")
                        add_int("Unknown")
                    count = add_byte("count")
                    for i in range(count):
                        add_byte("Unknown")
            add_field("Unknown", 26)"""
            decode_item(id)
elif f == 2: # buy item response
    add_int("ShopItemId")
    add_int("Amount")
elif f == 4: # update shop (after buying item)
    # 04 89 00 B1 00 01 00 00 00 36 10 00 00 01 00
    add_int("ItemId")
    add_int("Amount")
    add_int("Price")
    add_short("Unknown") # 1, sometimes 2
elif f == 6: # end load shop
    add_short("Unknown") # 1
elif f == 7: # load sold item
    add_short("amount? (1)")
    add_int("index")
    id = add_int("ItemId")
    add_byte("Rarity?")
    add_long("Price")
    decode_item(id)
elif f == 8: # rebuy sold item
    add_int("index")
elif f == 9: # pay for restock, response
    add_byte("Unknown")

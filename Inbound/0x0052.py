from script_api import *
from common import *

# 05 6E 9F D4 DB 71 98 CB 27 87 00 00 00 [f] [uid] [amount] (sell item)
# 03 01 00 00 00 [f] [index] (rebuy)
f = AddByte("function")

if f == 0: # Start load shop
    AddInt("NpcId")
    AddInt("ShopId")
    AddLong("ResetTime")
    AddInt("Unknown")
    AddShort("ItemCount")
    AddInt("Unknown+31") # 5
    AddByte("Unknown+35")
    AddBool("Unknown+36")
    canRestock = AddBool("CanRestock") # button for restocking
    AddBool("Unknown+38")
    AddByte("Unknown+39")
    AddBool("Unknown+40")
    AddBool("Unknown+41")
    AddBool("Unknown+42")
    AddBool("Unknown+43")
    AddString("shop name")
    if canRestock:
        AddByte("Unknown+46")
        AddByte("Unknown+47")
        AddInt("Unknown+48")
        AddInt("InstantRestockCost")
        AddBool("Unknown+56")
        AddInt("Unknown+57")
        AddByte("Unknown+61!") # important
        AddBool("Unknown+62")
        AddBool("Unknown+63")
elif f == 1: # add shop item
    count = AddByte("count")
    for i in range(count):
        with Node("Item " + str(i), i == 0):
            AddInt("ShopItemId")
            id = AddInt("ItemId")
            AddByte("Unknown") # 1
            AddInt("CurrencyId")
            AddInt("Unknown") # 0
            AddLong("Price")
            #AddInt("Unknown")
            AddByte("Rarity")
            AddInt("random num")
            AddInt("MaxStock?") # 0 = infinite
            AddInt("TotalSold")
            AddInt("Unknown")
            AddString("ShopCategory")
            AddInt("AchievmentRequired")
            AddInt("Unknown")
            AddByte("Unknown")
            AddShort("Unkown")
            AddByte("Unknown")
            AddShort("Unkown")
            AddBool("Unknown")
            AddShort("Unkown") # 1
            AddByte("Unkown") # 1
            AddByte("Unkown") # 1 (Has currency id str?)
            AddString("CurrencyIdStr")
            AddShort("Unkown")
            AddInt("Unknown")
            AddBool("Unknown")
            b = AddBool("Unknown")
            if b:
                pass

            """AddByte("Unknown")
            AddByte("Unknown")
            b = AddBool("Unknown")
            if b:
                b = AddBool("Unknown")
                if b:
                    AddLong("Unknown")
                    AddLong("Unknown")
                b = AddBool("Unknown")
                if b:
                    count = AddByte("count")
                    for i in range(count):
                        AddInt("Unknown")
                        AddInt("Unknown")
                    count = AddByte("count")
                    for i in range(count):
                        AddByte("Unknown")
            AddField("Unknown", 26)"""
            DecodeItem(id)
elif f == 2: # buy item response
    AddInt("ShopItemId")
    AddInt("Amount")
elif f == 4: # update shop (after buying item)
    # 04 89 00 B1 00 01 00 00 00 36 10 00 00 01 00
    AddInt("ItemId")
    AddInt("Amount")
    AddInt("Price")
    AddShort("Unknown") # 1, sometimes 2
elif f == 6: # end load shop
    AddShort("Unknown") # 1
elif f == 7: # load sold item
    AddShort("amount? (1)")
    AddInt("index")
    id = AddInt("ItemId")
    AddByte("Rarity?")
    AddLong("Price")
    DecodeItem(id)
elif f == 8: # rebuy sold item
    AddInt("index")
elif f == 9: # pay for restock, response
    AddByte("Unknown")

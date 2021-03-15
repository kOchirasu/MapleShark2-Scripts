from script_api import *
from common import *

def DecodeBlackMarketEntry():
    with Node("Entry"):
        AddLong("ListingUid")
        AddLong("TimeListed")
        AddLong("TimeListed")
        AddLong("TimeExpires")
        AddInt("Amount")
        AddInt("Unknown") # 0
        AddLong("CostPerItem")
        AddByte("Unknown") # 0
        AddLong("ItemUid")
        id = AddInt("ItemId")
        AddByte("Rarity")
        AddLong("ListerAccountId")
        DecodeItem(id)


f = AddByte("function")
if f == 0: # item sold out
    AddByte("Unknown")
    n = AddInt("ErrorCode")
    AddLong("ListingUid")
    AddInt("Unknown") # 0
    AddInt("Unknown") # 0
elif f == 1: # my listings
    count = AddInt("count")
    for i in range(count):
        DecodeBlackMarketEntry()
elif f == 2:
    DecodeBlackMarketEntry()
elif f == 3: # remove my listing
    AddLong("ListingUid")
    AddByte("Unknown") # 0
elif f == 4:
    count = AddInt("count")
    for i in range(count):
        DecodeBlackMarketEntry()
elif f == 5: # listing purchased
    AddLong("ListingUid")
    AddInt("Amount")
elif f == 6:
    AddByte("Unknown")
    AddLong("Unknown")
    AddLong("Unknown")
elif f == 7: # item sold
    pass # none
elif f == 8: # preview item
    AddInt("ItemId")
    AddInt("Rarity")
    AddLong("ShopPrice")
elif f == 9:
    pass

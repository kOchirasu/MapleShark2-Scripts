from script_api import *
from common import *

def decode_black_market_entry():
    with Node("Entry"):
        add_long("ListingUid")
        add_long("TimeListed")
        add_long("TimeListed")
        add_long("TimeExpires")
        add_int("Amount")
        add_int("Unknown") # 0
        add_long("CostPerItem")
        add_byte("Unknown") # 0
        add_long("ItemUid")
        id = add_int("ItemId")
        add_byte("Rarity")
        add_long("ListerAccountId")
        decode_item(id)


f = add_byte("function")
if f == 0: # item sold out
    add_byte("Unknown")
    n = add_int("ErrorCode")
    add_long("ListingUid")
    add_int("Unknown") # 0
    add_int("Unknown") # 0
elif f == 1: # my listings
    count = add_int("count")
    for i in range(count):
        decode_black_market_entry()
elif f == 2:
    decode_black_market_entry()
elif f == 3: # remove my listing
    add_long("ListingUid")
    add_byte("Unknown") # 0
elif f == 4:
    count = add_int("count")
    for i in range(count):
        decode_black_market_entry()
elif f == 5: # listing purchased
    add_long("ListingUid")
    add_int("Amount")
elif f == 6:
    add_byte("Unknown")
    add_long("Unknown")
    add_long("Unknown")
elif f == 7: # item sold
    pass # none
elif f == 8: # preview item
    add_int("ItemId")
    add_int("Rarity")
    add_long("ShopPrice")
elif f == 9:
    pass

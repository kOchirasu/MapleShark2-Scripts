from script_api import *

def decode_meso_market_entry():
    with Node("Entry"):
        add_long("ListingUid")
        add_long("MesoAmount")
        add_long("Cost")
        add_long("TimeListed")
        add_long("TimeExpires")
        add_bool("IsOwnListing") # self?


f = add_byte("function")
if f == 0:
    add_int("ErrorCode")
elif f == 1: # load market
    add_float("UnknownF") # 0
    add_float("UnknownF") # 0.2
    add_long("Cost")
    add_int("MaxListings?")
    add_int("MaxListings?")
    add_int("WeeklyLimit")
    add_int("Unknown") # 2? (order by?)
    add_int("AveragePrice")
    add_int("MaxListingsShown")
    add_int("Unknown") # 1000
elif f == 2: # load stats
    add_int("daily listed")
    add_int("monthly purchased")
elif f == 4: #  my listings
    count = add_int("count")
    for i in range(count):
        add_long("ListingUid")
        decode_meso_market_entry()
elif f == 5: # list
    decode_meso_market_entry()
    add_int("Unknown")
elif f == 6: # cancel
    add_int("Unknown") # 0
    add_long("ListingUid")
elif f == 7: # search results
    count = add_int("count")
    for i in range(count):
        decode_meso_market_entry()
elif f == 8:
    add_int("Unknown")
    add_long("Unknown")
    add_int("Unknown")

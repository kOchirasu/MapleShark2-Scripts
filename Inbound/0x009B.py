from script_api import *

def DecodeMesoMarketEntry():
    with Node("Entry"):
        AddLong("ListingUid")
        AddLong("MesoAmount")
        AddLong("Cost")
        AddLong("TimeListed")
        AddLong("TimeExpires")
        AddBool("IsOwnListing") # self?


f = AddByte("function")
if f == 0:
    AddInt("ErrorCode")
elif f == 1: # load market
    AddFloat("UnknownF") # 0
    AddFloat("UnknownF") # 0.2
    AddLong("Cost")
    AddInt("MaxListings?")
    AddInt("MaxListings?")
    AddInt("WeeklyLimit")
    AddInt("Unknown") # 2? (order by?)
    AddInt("AveragePrice")
    AddInt("MaxListingsShown")
    AddInt("Unknown") # 1000
elif f == 2: # load stats
    AddInt("daily listed")
    AddInt("monthly purchased")
elif f == 4: #  my listings
    count = AddInt("count")
    for i in range(count):
        AddLong("ListingUid")
        DecodeMesoMarketEntry()
    pass # none
elif f == 5: # list
    DecodeMesoMarketEntry()
    AddInt("Unknown")
elif f == 6: # cancel
    AddInt("Unknown") # 0
    AddLong("ListingUid")
elif f == 7: # search results
    count = AddInt("count")
    for i in range(count):
        DecodeMesoMarketEntry()
elif f == 8:
    AddInt("Unknown")
    AddLong("Unknown")
    AddInt("Unknown")

from script_api import *

f = AddByte("function")

if f == 3: # open market
    pass # none
elif f == 5: # list mesos
    AddLong("MesosAmount")
    AddLong("ListingPrice")
elif f == 6: # collect listing
    AddLong("ListingUid")
elif f == 7: # search?
    AddLong("MinAmount")
    AddLong("MaxAmount")
elif f == 8: # purchase
    AddLong("ListingUid")

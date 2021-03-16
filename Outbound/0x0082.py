from script_api import *

f = add_byte("function")

if f == 3: # open market
    pass # none
elif f == 5: # list mesos
    add_long("MesosAmount")
    add_long("ListingPrice")
elif f == 6: # collect listing
    add_long("ListingUid")
elif f == 7: # search?
    add_long("MinAmount")
    add_long("MaxAmount")
elif f == 8: # purchase
    add_long("ListingUid")

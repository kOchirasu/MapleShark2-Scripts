''' REQUEST_RIDE '''
from script_api import *
from item import *

f = add_byte("Function")
if f == 0: # Start Ride
    add_byte("type")
    add_int("MountId") # ItemData => ride.rideMonster
    add_int("Unknown") # ObjectId?
    add_int("ItemId") # 0 (unset)
    add_long("ItemUid") # 0 (unset)
    decode_ugc_item_look()
elif f == 1: # Stop Ride
    add_byte("RideOffAction+12") # state? (15 = no ride)
    add_bool("forced") # Going into water without amphibious riding
elif f == 2: # Change Ride
    add_int("MountId")
    add_long("MountUid")
elif f == 3: # Start RideShareAuthority
    add_int("objectId")
elif f == 4: # Stop RideShareAuthority
    pass

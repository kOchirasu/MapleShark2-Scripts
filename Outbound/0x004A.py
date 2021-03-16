from script_api import *

f = add_byte("function")
if f == 0: # request trade
    add_long("CharacterId")
elif f == 2: # got trade request
    add_long("CharacterId")
elif f == 3: # accept trade
    add_long("CharacterId")
elif f == 4: # decline trade
    add_long("CharacterId")
elif f == 5:
    add_long("Unknown")
elif f == 7: # cancel trade
    pass # none
elif f == 8: # Add item
    add_long("ItemUid")
    add_int("Amount")
    add_int("Slot")
elif f == 9: # Remove item
    add_long("ItemUid")
    add_int("Slot")
elif f == 10: # Set mesos
    add_long("Mesos")
elif f == 11: # finalize trade
    pass # none
elif f == 13: # confirm finalize trade
    pass # none

from script_api import *

f = AddByte("function")
if f == 0: # request trade
    AddLong("CharacterId")
elif f == 2: # got trade request
    AddLong("CharacterId")
elif f == 3: # accept trade
    AddLong("CharacterId")
elif f == 4: # decline trade
    AddLong("CharacterId")
elif f == 5:
    AddLong("Unknown")
elif f == 7: # cancel trade
    pass # none
elif f == 8: # Add item
    AddLong("ItemUid")
    AddInt("Amount")
    AddInt("Slot")
elif f == 9: # Remove item
    AddLong("ItemUid")
    AddInt("Slot")
elif f == 10: # Set mesos
    AddLong("Mesos")
elif f == 11: # finalize trade
    pass # none
elif f == 13: # confirm finalize trade
    pass # none

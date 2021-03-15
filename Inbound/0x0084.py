from script_api import *
from common import *

f = AddByte("function")
if f == 0: # Receive trade request
    AddUnicodeString("PlayerName")
    AddLong("CharacterId")
elif f == 1: # unknown
    AddByte("Unknown")
    AddUnicodeString("UnknownStr")
    AddInt("Unknown")
    AddInt("Unknown")
elif f == 2: # confirm request trade
    pass # none
elif f == 4: # trade declined
    AddUnicodeString("PlayerName")
elif f == 5: # begin trade
    AddLong("CharacterId")
elif f == 6: # end trade
    AddBool("Success")
elif f == 8: # Add item
    AddByte("Unknown") # 1
    id = AddInt("ItemId")
    AddLong("ItemUid")
    AddInt("Unknown") # 1
    AddInt("TradeSlot")
    AddInt("Amount")
    AddInt("Unknown")
    DecodeItem(id)
elif f == 9: # RemoveItem
    AddByte("Unknown")
    AddInt("TradeSlot")
    AddLong("ItemUid")
elif f == 10: # set money
    AddByte("Unknown")
    AddLong("Mesos")
elif f == 11: # finalize trade
    AddByte("Unknown") # (0 = left, 1 = right)
elif f == 13: # finalize confirm trade
    AddByte("Unknown") # (0 = left, 1 = right)
elif f == 12:
    t = AddByte("Unknown")
    if t == 1:
        pass # ...
elif f == 13 or f == 14:
    pass

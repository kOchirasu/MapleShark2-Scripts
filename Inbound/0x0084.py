from script_api import *
from common import *

f = add_byte("function")
if f == 0: # Receive trade request
    add_unicode_str("PlayerName")
    add_long("CharacterId")
elif f == 1: # unknown
    add_byte("Unknown")
    add_unicode_str("UnknownStr")
    add_int("Unknown")
    add_int("Unknown")
elif f == 2: # confirm request trade
    pass # none
elif f == 4: # trade declined
    add_unicode_str("PlayerName")
elif f == 5: # begin trade
    add_long("CharacterId")
elif f == 6: # end trade
    add_bool("Success")
elif f == 8: # Add item
    add_byte("Unknown") # 1
    id = add_int("ItemId")
    add_long("ItemUid")
    add_int("Unknown") # 1
    add_int("TradeSlot")
    add_int("Amount")
    add_int("Unknown")
    decode_item(id)
elif f == 9: # RemoveItem
    add_byte("Unknown")
    add_int("TradeSlot")
    add_long("ItemUid")
elif f == 10: # set money
    add_byte("Unknown")
    add_long("Mesos")
elif f == 11: # finalize trade
    add_byte("Unknown") # (0 = left, 1 = right)
elif f == 13: # finalize confirm trade
    add_byte("Unknown") # (0 = left, 1 = right)
elif f == 12:
    t = add_byte("Unknown")
    if t == 1:
        pass # ...
elif f == 13 or f == 14:
    pass

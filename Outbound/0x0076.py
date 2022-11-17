''' CHANGE_ATTRIBUTES '''
from script_api import *

f = add_byte("function")
if f == 0: # Change attributes
    add_long("ItemUid")
    add_long("Unknown")
    b = add_bool("UseLock")
    if b:
        add_byte("IsSpecialAttribute")
        add_short("AttributeType")
elif f == 2: # Select new option
    add_long("ItemUid")
elif f == 5:
    add_long("ItemUid")
    add_long("Unknown")
    b = add_bool("UseLock")
    if b:
        add_byte("IsSpecialAttribute")
        add_short("AttributeType")
    
    add_bool("unknown")
    add_int("unknown")
elif f == 6: # CCItemRemakeOptionPacket::ForceFillIngredient
    add_long("ItemUid")
    add_int("count?")

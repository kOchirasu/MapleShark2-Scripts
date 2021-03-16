from script_api import *
from common import *

f = add_byte("function")

if f == 4:
    add_str("EntityId")
    add_byte("Unknown") # 0 <- visible?
    add_byte("Unknown") # 1
elif f == 5: # after interacting, despawn?
    add_str("EntityId")
    add_byte("Unknown") # 6 (index?)
    # ... (00 00 01 00 00 00)
elif f == 6:
    add_int("InteractId")
    add_byte("Unknown")
elif f == 7:
    add_byte("Unknown")
elif f == 8:
    count = add_int("count")
    for i in range(count):
        with Node("Interact " + str(i)):
            add_str("EntityId")
            add_byte("Unknown")
            b = add_byte("Unknown")
            if b == 6:
                add_int("Unknown")
elif f == 9:
    add_str("Name") # EventCreate_982795
    add_byte("Unknown")
    add_byte("Unknown")
    add_int("InteractObjectId")
    decode_coordF("Position")
    decode_coordF("Rotation")
    add_unicode_str("InteractXmlType") # MS2InteractActor/MS2InteractMesh
    add_unicode_str("UnknownStr") # interaction_chestA_02
    add_unicode_str("UnknownStr") # Opened_A/Interaction_advertisement_A01
    add_unicode_str("UnknownStr") # Idle_A/Interaction_advertisement_A01
    add_float("Unknown")
    add_bool("Unknown")
    # Some other conditional cases
    add_long("Unknown")
    add_unicode_str("OwnerIgn")
elif f == 10:
    add_str("Unknown")
    add_unicode_str("Unknown")
elif f == 13: # respawn? | gold chest remove #2
    add_byte("Unknown") # 0 <- visible?
    add_str("EntityId")
    add_byte("Unknown") # index? (6, 1)
    # ...?
elif f == 14:
    add_short("Unknown")
    add_int("Unknown")
    add_int("Unknown")
    add_unicode_str("Unknown")
elif f == 15:
    add_int("Unknown")
    add_int("Unknown")

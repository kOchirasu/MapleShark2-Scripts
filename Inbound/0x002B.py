from script_api import *
from common import *

add_int("ObjectId")
id = add_int("ItemId")
add_int("Amount")
b = add_bool("Flag")
if b:
    add_long("Uid")
decode_coordF("")
add_int("LooterObjectId")
add_int("Unknown")
add_byte("Unknown")
add_int("Rarity")
add_short("Unknown")
add_byte("Unknown")
add_byte("Unknown")
# No info for mesos...
if id != 90000001:
    decode_item(id)

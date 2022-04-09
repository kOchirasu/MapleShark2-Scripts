''' FIELD_ADD_ITEM '''
from script_api import *
from common import *

add_int("ObjectId")
id = add_int("ItemId")
add_int("Amount")
b = add_bool("flag")
if b:
    add_long("Uid")
decode_coordF("position")
add_int("ownerObjectId")
add_int("Unknown")
add_byte("Unknown")
add_int("Rarity")
add_short("Unknown")
add_bool("Unknown")
add_bool("Unknown")
# No info for mesos...
if id < 90000001 or id > 90000003:
    decode_item(id)

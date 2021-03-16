from script_api import *
from common import *

add_int("UserObjectId")
id = add_int("ItemId")
add_long("ItemUid")
add_unicode_str("EquipSlot")
add_int("Rarity?")
add_byte("Unknown")
decode_item(id)

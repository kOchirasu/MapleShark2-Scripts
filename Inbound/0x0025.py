''' ITEM_PUT_ON '''
from script_api import *
from item import *

add_int("UserObjectId")
id = add_int("ItemId")
add_long("ItemUid")
add_unicode_str("EquipSlot")
add_int("Rarity")
add_byte("Unknown") # 0, 1, 2, rest invalid
decode_item(id)

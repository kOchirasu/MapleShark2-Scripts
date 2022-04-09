''' ITEM_SKIN_PUT_OFF '''
from script_api import *
from common import *

add_int("UserObjectId")
id = add_int("ItemId")
add_long("ItemUid")
add_long("Rarity")
add_long("Slot")
decode_item(id)

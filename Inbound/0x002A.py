''' ITEM_UPDATE '''
from script_api import *
from item import *

# Seems to be used to update the existing item on a player (e.g. changing hair)
add_int("PlayerObjectId")
add_long("ItemUid")
decode_item(10200000) # this is the itemId corresponding to uid

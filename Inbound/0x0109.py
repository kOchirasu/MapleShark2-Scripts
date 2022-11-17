''' ITEM_EXTRACTION '''
from script_api import *
from item import *

f = add_byte("function")
if f == 0: # s_itemextraction_success
    add_long("ItemUid")
    add_long("CreatedItemUid")
    add_short("Unknown")
    decode_equip_color()
    decode_item_transfer()
elif f == 1:
    pass # s_itemextraction_inventoryfull
elif f == 2:
    pass # s_itemextraction_lack_scroll

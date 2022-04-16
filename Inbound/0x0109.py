from script_api import *
from item import *

f = add_byte("function")
if f == 0:
    add_long("ItemUid")
    add_long("CreatedItemUid")
    add_short("Unknown")
    decode_equip_color()

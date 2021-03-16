from script_api import *
from common import *

f = add_byte("function")
if f == 1:
    add_long("ItemUid")
    decode_item(0)
elif f == 2:
    add_long("ItemUid")
    decode_item(0)
elif f == 4:
    add_byte("Unknown")
    add_int("Unknown")

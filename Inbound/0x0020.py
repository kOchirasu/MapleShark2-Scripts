''' ITEM_PUT_ON_OR_OFF '''
from script_api import *

f = add_byte("function")
if f == 2:
    add_long("ItemUid")
elif f == 3:
    add_long("ItemUid")
elif f == 5:
    add_int("unknown")
    add_long("ItemUid")
    add_unicode_str("unknown")
    add_byte("unknown")
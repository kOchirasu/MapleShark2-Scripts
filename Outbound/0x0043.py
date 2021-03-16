from script_api import *

f = add_byte("function")
if f == 2: # put on item
    add_long("ItemUid")
    add_long("AccountUid")
    add_unicode_str("Slot")
elif f == 3: # swap outfits
    add_long("DollUid")
elif f == 7: # remove item
    add_long("ItemUid")
    add_unicode_str("Slot")
elif f == 10: # remove doll
    add_long("DollUid")

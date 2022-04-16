''' FURNISHING_STORAGE '''
from script_api import *
from item import *

f = add_byte("Function")
if f == 1: # start list
    pass
elif f == 2: # count
    add_int("storage count")
elif f == 3: # add
    id = add_int("ItemId")
    add_long("ItemUid")
    add_byte("rarity")
    add_int("slot")
    decode_item(id)
elif f == 4: # remove
    add_long("ItemUid")
elif f == 5: # purchase
    add_long("ItemUid")
    add_int("Count")
elif f == 7: # update
    add_long("ItemUid")
    add_int("Count")
elif f == 8: # end list
    pass # noop actually

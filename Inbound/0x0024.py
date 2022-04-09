''' FURNISHING_INVENTORY '''
from script_api import *
from common import *

f = add_byte("function")
if f == 0: # start list
    pass
elif f == 1:
    add_int("ItemId")
    add_long("ItemUid")
    add_long("Unknown")
    b = add_bool("IsTemplate")
    if b:
        decode_ugc_data()
elif f == 2: # Remove
    add_long("ItemUid")
elif f == 3: # Update
    add_long("ItemUid")
    add_int("Count")
elif f == 4: # end list
    pass # noop actually

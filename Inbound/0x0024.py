from script_api import *
from common import *

count = add_byte("function")
if count == 0 or count == 4:
    # 0 == Start List
    # 4 == End List
    pass
elif count == 1:
    add_int("ItemId")
    add_long("ItemUid")
    add_long("Unknown")
    b = add_bool("IsTemplate")
    if b:
        decode_ugc_data()

elif count == 2: # Remove
    add_long("ItemUid")
elif count == 3: # Update?
    add_long("ItemUid")
    add_int("Count")

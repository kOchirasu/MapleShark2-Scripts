from script_api import *
from common import *

f = add_byte("Function")
if f == 2: # opening furnishing box
    add_int("storage count")
elif f == 3:
    id = add_int("ItemId")
    add_long("ItemUid")
    add_byte("rarity")
    add_int("Index")
    decode_item(id)
elif f == 4:
    add_long("ItemUid")
elif f == 5: # opening furnishing box
    add_long("ItemUid")
    add_int("Count")
elif f == 7: # opening furnishing box
    add_long("ItemUid")
    add_int("Count")

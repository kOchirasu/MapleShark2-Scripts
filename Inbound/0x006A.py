from script_api import *
from common import *

def decode_cube_item_info():
    with Node("CubeItemInfo"):
        add_int("ItemId")
        add_long("ItemUid")
        add_long("Unknown")
        b = add_bool("IsUgc")
        if b:
            decode_ugc_data()
    

# BROADCASTED
add_int("PlayerObjectId")
b = add_bool("IsStart")
if b:
    decode_cube_item_info()
    add_int("Unknown")

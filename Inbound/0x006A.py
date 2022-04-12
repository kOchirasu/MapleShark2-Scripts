''' SET_CRAFT_MODE '''
from script_api import *
from common import *

# BROADCASTED
add_int("PlayerObjectId")
b = add_bool("IsStart")
if b:
    decode_cube_item_info()
    add_int("Unknown")

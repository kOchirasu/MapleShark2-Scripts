from script_api import *
from common import *
    

add_byte("function") # this is also 0/1 but it's redundant
b = add_bool("IsStart")
if b:
    decode_cube_item_info()

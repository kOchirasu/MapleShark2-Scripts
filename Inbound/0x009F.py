from script_api import *
from common import *

f = add_byte("Function")

if f == 0: # add maid
    add_bool("Unknown") # num here is kinda random
    decode_maid()
elif f == 1: # Remove maid
    add_long("ItemUid")

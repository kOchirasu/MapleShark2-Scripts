from script_api import *
from common import *

f = add_byte("Function")

if f == 0: # load maid info (loads all purchased maids?)
    count = add_int("count")
    for i in range(count):
        add_bool("Unknown") # 1
        decode_maid()
elif f == 1: # add maid to map
    add_bool("Unknown")  # 1
    decode_maid()
elif f == 2:
    add_long("Unknown")
elif f == 3: # add maid to house
    add_bool("Unknown")  # 1
    decode_maid()
elif f == 4:
    add_int("Unknown")

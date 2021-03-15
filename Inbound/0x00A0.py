from script_api import *
from common import *

f = AddByte("Function")

if f == 0: # load maid info (loads all purchased maids?)
    count = AddInt("count")
    for i in range(count):
        AddBool("Unknown") # 1
        DecodeMaid()
elif f == 1: # add maid to map
    AddBool("Unknown")  # 1
    DecodeMaid()
elif f == 2:
    AddLong("Unknown")
elif f == 3: # add maid to house
    AddBool("Unknown")  # 1
    DecodeMaid()
elif f == 4:
    AddInt("Unknown")

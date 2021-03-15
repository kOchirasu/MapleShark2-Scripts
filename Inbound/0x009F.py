from script_api import *
from common import *

f = AddByte("Function")

if f == 0: # add maid
    AddBool("Unknown") # num here is kinda random
    DecodeMaid()
elif f == 1: # Remove maid
    AddLong("ItemUid")

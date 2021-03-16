from script_api import *
from common import *

# Request 0x0025 08 (SendJob)
# Response This packet
add_int("ObjectId")
f = add_byte("function") # 2 for awakening?
if f != 0:
    decode_skill_tree()

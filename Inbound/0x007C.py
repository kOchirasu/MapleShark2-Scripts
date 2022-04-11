from script_api import *
from common import *

add_int("ObjectId")
count = add_byte("Count")
for i in range(count):
    decode_state_sync()

from script_api import *
from common import *

add_short("Type")
count = add_byte("segments")
for i in range(count):
    decode_state_sync()
add_int("ClientTick")
add_int("ServerTick")

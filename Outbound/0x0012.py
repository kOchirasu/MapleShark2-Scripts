from script_api import *
from common import *

add_byte("Function")
add_int("ServerTick")
add_int("ClientTicks")
count = add_byte("segments")
for i in range(count):
    with Node("Segment " + str(i), True):
        decode_state_sync()
        add_int("ClientTicks")
        add_int("ServerTick")

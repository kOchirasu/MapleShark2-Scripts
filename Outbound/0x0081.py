from script_api import *
from common import *

f = add_byte("Function")
add_byte("State")
add_int("ServerTick")
if f == 0:
    decode_coordF("Position")
elif f == 1:
    pass # nothing

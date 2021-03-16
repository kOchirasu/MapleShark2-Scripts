from script_api import *
from common import *

f = add_byte("Function")
if f == 0:
    add_int("MapId")
    add_byte("Unknown")
    add_byte("Unknown")
    add_int("Unknown")
    add_int("Unknown")
    decode_coordF("Position")
    decode_coordF("Rotation")
    add_int("Unknown")

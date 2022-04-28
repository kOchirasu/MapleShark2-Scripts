''' REQUEST_FIELD_ENTER '''
from script_api import *
from common import *

message = add_byte("message")
if message == 0: # OK
    add_int("MapId")
    add_byte("Unknown")
    add_byte("Unknown")
    add_int("Unknown")
    add_int("Unknown")
    decode_coordF("Position")
    decode_coordF("Rotation")
    add_int("Unknown")

# some reference to the same error messages in MOVE_RESULT
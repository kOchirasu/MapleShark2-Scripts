''' REQUEST_FIELD_ENTER '''
from script_api import *
from common import *

message = add_byte("message")
if message == 0: # OK
    add_int("MapId") # Used to lookup taxis
    add_byte("Unknown") # Party related
    add_byte("Unknown") # Learning quest related (guide)
    add_int("Unknown") # Learning quest related (guide)
    add_int("Unknown") # Dungeon id
    decode_coordF("Position")
    decode_coordF("Rotation")
    add_int("Unknown") # Same value in ResponseFieldEnter

# some reference to the same error messages in MOVE_RESULT
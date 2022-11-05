''' GAME_TO_GAME '''
from script_api import *

message = add_byte("message")
if message == 0: # OK
    add_int("MigrationTokenA")
    add_int("MigrationTokenB")
    add_int("IpAddress")
    add_short("Port")
    add_int("MapId")
    add_byte("Unknown")

# some reference to the same error messages in MOVE_RESULT
''' GAME_TO_LOGIN '''
from script_api import *

message = add_byte("message")
if message == 0: # OK
    add_int("IPAddress")
    add_short("Port")
    add_long("MigrationToken")

# some reference to the same error messages in MOVE_RESULT
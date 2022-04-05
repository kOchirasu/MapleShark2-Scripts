''' LOGIN_TO_GAME '''
from script_api import *

message = add_byte("message")
if message == 0: # OK
    add_int("IPAddress")
    add_short("Port")
    add_long("MigrationToken")
    add_int("MapId")
else: # error
    add_unicode_str("message")

if message == 49:
    add_long("unknown")

# some reference to the same error messages in MOVE_RESULT
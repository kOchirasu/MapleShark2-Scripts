''' RESPONSE_TIME_SYNC '''
from script_api import *

f = add_byte("function")
if f == 0: # initalize
    add_int("ServerTick")
    add_long("Timestamp")
    add_int("TimeOffset")
    add_byte("Unknown")
    add_int("some ObjectId") # this is usually 0
elif f == 1: # resets other fields
    add_int("ServerTick")
    add_long("Timestamp")
    add_int("TimeOffset")
    add_byte("Unknown")
elif f == 2: # request sync
    pass
elif f == 3: # set time
    add_long("Timestamp")

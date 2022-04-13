''' RESPONSE_TIME_SYNC '''
from script_api import *

f = add_byte("function")
if f == 0: # initalize
    add_int("ServerTick")
    add_long("Timestamp")
    add_int("TimeOffset")
    add_byte("Timezone")
    add_int("key") # client sends this in request
elif f == 1: # resets fields instead of using "key"
    add_int("ServerTick")
    add_long("Timestamp")
    add_int("TimeOffset")
    add_byte("Timezone")
elif f == 2: # request sync
    pass
elif f == 3: # set time
    add_long("Timestamp")

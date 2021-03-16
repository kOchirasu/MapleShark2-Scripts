from script_api import *

f = add_byte("function")
add_byte("Unknown") # 1

if f == 0: # close recall
    pass # none
elif f == 1: # open recall
    add_unicode_str("PlayerName") # player who used the scroll
    add_int("Unknown") # 1
    add_int("MapId")
    add_int("Unknown") # Random ticks? (Unknown)
    add_long("Timestamp")

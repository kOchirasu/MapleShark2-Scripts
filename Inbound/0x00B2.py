from script_api import *

f = add_byte("Function")
if f == 0: # world boss spawn map
    add_int("BossMonsterId")
    add_int("MapId")
    add_short("Channel?")
    add_long("Timestamp")
    add_bool("Alive?") # 1

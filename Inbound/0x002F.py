''' STAT '''
from script_api import *
from stats import *

add_int("objectId")
add_byte("Function") # don't know what this actually does 0/1?

# NOTE: parsing logic is an appoximation since we have no way to know
# if an entity is MyPC, PC or NPC. See stats.py for details.
count = add_byte("count")
if count == 1:
    decode_specific_stat()
elif count == 35:
    if remaining() > 72: # (8+4+4+4+4) * 3
        for i in range(35):
            with Node("Stat " + str(i)):
                decode_stat(i)
    else:
        decode_player_delta_stats()
else:
    if remaining() > 36: # (8+4) * 3
        for i in range(count):
            with Node("Stat " + str(i), True):
                decode_specific_stat()
    else:
        decode_npc_delta_stats()

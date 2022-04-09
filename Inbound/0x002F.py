''' STAT '''
from script_api import *

def decode_stat(statType):
    if statType == 4: # Hp
        add_long("TotalHp")
        add_long("MinHp")
        add_long("MaxHp")
    else:
        add_int("StatTotal")
        add_int("StatMin")
        add_int("StatMax")

def decode_specific_stat():
    statType = add_byte("StatType")
    decode_stat(statType)

def decode_specific_stats(count):
    for i in range(count):
        with Node("Stat " + str(i), True):
            decode_specific_stat()

def decode_player_delta_stats():
    for i in range(3):
        with Node("Stats " + str(i), True):
            add_long("Health")
            add_int("AtkSpd")
            add_int("MoveSpd")
            add_int("MountSpd")
            add_int("JumpHeight")

def decode_npc_delta_stats():
    for i in range(3):
        with Node("Stats " + str(i), True):
            add_long("Health")
            add_int("AtkSpd")


add_int("objectId")
add_byte("Function") # don't know what this actually does 0/1?

# NOTE: parsing logic is an appoximation since we have no way to know
# if an entity is MyPC, PC or NPC. See below comments for details.
t = add_byte("StatType")
if t == 1:
    decode_specific_stat()
elif t == 35:
    if remaining() > 72: # (8+4+4+4+4) * 3
        for i in range(35):
            with Node("Stat " + str(i)):
                decode_stat(i)
    else:
        decode_player_delta_stats()
else:
    if remaining() > 36: # (8+4) * 3
        decode_specific_stats(t)
    else:
        decode_npc_delta_stats()

''' MyPC
if t == 35:
    for i in range(35):
        with Node("Stat " + str(i)):
            decode_stat(i)
else:
    decode_specific_stats(t)
'''

''' PC
if t == 35:
    decode_player_delta_stats()
else:
    decode_specific_stats(t)
'''

''' NPC
if t == 1:
    decode_specific_stat()
else:
    decode_npc_delta_stats()
'''

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

def decode_player_delta_stats():
    for i in {"Total", "Min", "Max"}:
        with Node(i, True):
            add_long("Health")
            add_int("AtkSpd")
            add_int("MoveSpd")
            add_int("MountSpd")
            add_int("JumpHeight")

def decode_npc_delta_stats():
    for i in {"Total", "Min", "Max"}:
        with Node(i, True):
            add_long("Health")
            add_int("AtkSpd")


''' Decode functions per type '''
def decode_npc_stats(): # class CNpc
    with Node("NpcStats"):
        count = add_byte("count")
        if count == 1:
            decode_specific_stat()
        else:
            decode_npc_delta_stats()

# this is for other players
def decode_player_stats(): # class PC
    with Node("PlayerStats"):
        count = add_byte("count")
        if count == 35:
            decode_player_delta_stats()
        else:
            for i in range(count):
                with Node("Stat " + str(i), True):
                    decode_specific_stat()

# this is for own player
def decode_my_player_stats(): # class MyPC
    with Node("MyPlayerStats"):
        count = add_byte("count")
        if count == 35:
            for i in range(35):
                with Node("Stat " + str(i), True):
                    decode_stat(i)
        else:
            for i in range(count):
                with Node("Stat " + str(i), True):
                    decode_specific_stat()

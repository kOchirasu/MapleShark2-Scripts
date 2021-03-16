from script_api import *

def decode_specific_stats(count):
    for i in range(count):
        with Node("Stat " + str(i), True):
            statType = add_byte("StatType")
            decode_stat(statType)

def decode_stat(statType):
    if statType == 4:
        add_long("TotalHp")
        add_long("MinHp")
        add_long("MaxHp")
    else:
        add_int("StatTotal")
        add_int("StatMin")
        add_int("StatMax")


add_int("uid")
f = add_byte("Function")
t = add_byte("StatType")
if f == 0:
    if t == 35:
        # Not parsing here because it differs between self and others
        for i in range(35):
            with Node("Stat " + str(i)):
                decode_stat(i)
    else:
        decode_specific_stats(t)
elif f == 1:
    if t == 35:
        for i in range(3):
            with Node("Stats " + str(i), True):
                add_long("Health")
                add_int("AtkSpd")
                add_int("MoveSpd")
                add_int("MountSpd")
                add_int("JumpHeight")
    else:
        decode_specific_stats(t)

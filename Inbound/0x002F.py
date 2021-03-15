from script_api import *

def DecodeSpecificStats(count):
    for i in range(count):
        with Node("Stat " + str(i), True):
            statType = AddByte("StatType")
            DecodeStat(statType)

def DecodeStat(statType):
    if statType == 4:
        AddLong("TotalHp")
        AddLong("MinHp")
        AddLong("MaxHp")
    else:
        AddInt("StatTotal")
        AddInt("StatMin")
        AddInt("StatMax")


AddInt("uid")
f = AddByte("Function")
t = AddByte("StatType")
if f == 0:
    if t == 35:
        # Not parsing here because it differs between self and others
        for i in range(35):
            with Node("Stat " + str(i)):
                DecodeStat(i)
    else:
        DecodeSpecificStats(t)
elif f == 1:
    if t == 35:
        for i in range(3):
            with Node("Stats " + str(i), True):
                AddLong("Health")
                AddInt("AtkSpd")
                AddInt("MoveSpd")
                AddInt("MountSpd")
                AddInt("JumpHeight")
    else:
        DecodeSpecificStats(t)

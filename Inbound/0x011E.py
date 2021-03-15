from script_api import *

f = AddByte("Function")

if f == 0:
    AddLong("PrestigeExp")
    AddInt("PrestigeLevel")
    AddLong("PrestigeExp")
    count = AddInt("Count")
    # 2, 4, 6, 8, 10, 12, 20, 30, 40, 50, 60, 70, 80, 90???
    for i in range(count):
        AddInt("ClaimedRankReward " + str(i))
elif f == 1: # Gain Prestige
    AddLong("CurrentPrestigeExp")
    AddLong("GainedPrestigeExp")
elif f == 2: # level up
    AddInt("UserObjectId")
    AddInt("PrestigeLevel")
elif f == 4:
    AddByte("Unknown")
    count = AddInt("count")
    for i in range(count):
        AddInt("Unknown")
#  6 is sent after box claimed, 7 is sent on load
elif f == 7: # same as 6
    count = AddInt("count")
    for i in range(count):
        with Node("WeeklyBox " + str(i), True):
            AddLong("BoxIndex")
            AddLong("WeeklyLevelsGained")
            AddBool("BoxClaimed")

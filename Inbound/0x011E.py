from script_api import *

f = add_byte("Function")

if f == 0:
    add_long("PrestigeExp")
    add_int("PrestigeLevel")
    add_long("PrestigeExp")
    count = add_int("Count")
    # 2, 4, 6, 8, 10, 12, 20, 30, 40, 50, 60, 70, 80, 90???
    for i in range(count):
        add_int("ClaimedRankReward " + str(i))
elif f == 1: # Gain Prestige
    add_long("CurrentPrestigeExp")
    add_long("GainedPrestigeExp")
elif f == 2: # level up
    add_int("UserObjectId")
    add_int("PrestigeLevel")
elif f == 4:
    add_byte("Unknown")
    count = add_int("count")
    for i in range(count):
        add_int("Unknown")
#  6 is sent after box claimed, 7 is sent on load
elif f == 7: # same as 6
    count = add_int("count")
    for i in range(count):
        with Node("WeeklyBox " + str(i), True):
            add_long("BoxIndex")
            add_long("WeeklyLevelsGained")
            add_bool("BoxClaimed")

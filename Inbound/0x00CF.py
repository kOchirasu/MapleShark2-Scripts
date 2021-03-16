from script_api import *

# SendMastery
f = add_byte("Function1")

if f == 0: # mastery exp
    add_byte("MasteryType")
    add_int("CurrentMastery")
    add_int("Unknown")
elif f == 1: # claiming rank reward
    add_int("RewardId")
    count = add_int("count")
    for i in range(count):
        add_int("ItemId")
        add_short("Rarity")
elif f == 2: # craft result
    add_short("MasteryType")
    count = add_int("count")
    for i in range(count):
        add_int("ItemId") # Reward from craft item
        add_short("Rarity")
elif f == 3: # error code?
    add_short("Unknown")

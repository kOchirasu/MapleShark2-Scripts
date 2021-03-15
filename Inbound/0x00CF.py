from script_api import *

# SendMastery
f = AddByte("Function1")

if f == 0: # mastery exp
    AddByte("MasteryType")
    AddInt("CurrentMastery")
    AddInt("Unknown")
elif f == 1: # claiming rank reward
    AddInt("RewardId")
    count = AddInt("count")
    for i in range(count):
        AddInt("ItemId")
        AddShort("Rarity")
elif f == 2: # craft result
    AddShort("MasteryType")
    count = AddInt("count")
    for i in range(count):
        AddInt("ItemId") # Reward from craft item
        AddShort("Rarity")
elif f == 3: # error code?
    AddShort("Unknown")

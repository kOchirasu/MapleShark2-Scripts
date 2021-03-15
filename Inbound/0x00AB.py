from script_api import *

def DecodeMaidCraft():
    AddLong("CraftUid") # 2867694360299044869
    AddLong("RecipeUid") # 2867553603835392936
    AddInt("RecipeId")
    AddLong("StartTimestamp")
    AddInt("CraftTimeSeconds")
    AddInt("CraftTimeSeconds")

f = AddByte("Function")
if f == 0: # active item crafts
    count = AddInt("count")
    for i in range(count):
        DecodeMaidCraft()
elif f == 1:
    DecodeMaidCraft()
elif f == 2:
    DecodeMaidCraft()
elif f == 3: # collect/cancel craft
    AddLong("RecipeUid")
elif f == 4: # craft item response #2
    AddInt("Amount?") # 1
elif f == 6: # collect item #3
    AddInt("Unknown") # 2
elif f == 7: # Same as 6
    AddInt("Unknown")
elif f == 8: # Same as 6
    AddInt("Unknown")
elif f == 9: # Same as 6
    AddInt("Unknown")
elif f == 10: # cancel craft #2
    AddInt("Unknown") # 4
elif f == 11: # collect item #2
    AddInt("ItemId")
    AddInt("Amount")
    AddByte("Rarity")
    AddInt("MoodIncrease")
    AddInt("ClosenessIncrease")
    AddByte("Unknown")
    AddByte("Unknown")

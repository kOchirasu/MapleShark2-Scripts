from script_api import *

def decode_maidCraft():
    add_long("CraftUid") # 2867694360299044869
    add_long("RecipeUid") # 2867553603835392936
    add_int("RecipeId")
    add_long("StartTimestamp")
    add_int("CraftTimeSeconds")
    add_int("CraftTimeSeconds")

f = add_byte("Function")
if f == 0: # active item crafts
    count = add_int("count")
    for i in range(count):
        decode_maidCraft()
elif f == 1:
    decode_maidCraft()
elif f == 2:
    decode_maidCraft()
elif f == 3: # collect/cancel craft
    add_long("RecipeUid")
elif f == 4: # craft item response #2
    add_int("Amount?") # 1
elif f == 6: # collect item #3
    add_int("Unknown") # 2
elif f == 7: # Same as 6
    add_int("Unknown")
elif f == 8: # Same as 6
    add_int("Unknown")
elif f == 9: # Same as 6
    add_int("Unknown")
elif f == 10: # cancel craft #2
    add_int("Unknown") # 4
elif f == 11: # collect item #2
    add_int("ItemId")
    add_int("Amount")
    add_byte("Rarity")
    add_int("MoodIncrease")
    add_int("ClosenessIncrease")
    add_byte("Unknown")
    add_byte("Unknown")

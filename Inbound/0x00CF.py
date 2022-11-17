''' MASTERY '''
from script_api import *

# SendMastery
f = add_byte("function")
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
    code = add_short("Unknown")
    if code == 1:
        pass # s_mastery_error_lack_mastery
    elif code == 2:
        pass # s_mastery_error_lack_meso
    elif code == 3:
        pass # s_mastery_error_lack_quest
    elif code == 4:
        pass # s_mastery_error_lack_item
    elif code == 5:
        pass # s_mastery_error_unknown
    elif code == 7:
        pass # s_mastery_error_invalid_level
    elif code == 12:
        pass # s_anti_addiction_cannot_receive

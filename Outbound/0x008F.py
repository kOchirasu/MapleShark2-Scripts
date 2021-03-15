from script_api import *

f = AddByte("function")

if f == 1: # open ui
    pass # none
elif f == 2: # claim reward
    AddInt("RewardId?")
elif f == 3: # open purchase
    pass # none
elif f == 4: # buy premium
    AddInt("OptionId")

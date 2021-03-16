from script_api import *

f = add_byte("function")

if f == 1: # open ui
    pass # none
elif f == 2: # claim reward
    add_int("RewardId?")
elif f == 3: # open purchase
    pass # none
elif f == 4: # buy premium
    add_int("OptionId")

from script_api import *

f = add_byte("function")

if f == 0: # activate premium
    add_int("UserObjectId")
    add_long("Premium expiration")
elif f == 1: # daily rewards
    m = add_int("flag?")
    if m != 0:
        m = add_int("Unknown")
        while m != 1:
            m = add_int("Unknown")
elif f == 2: # confirm reward claimed
    add_int("RewardId")
elif f == 3: # purchase options
    count = add_int("Count")
    for i in range(count):
        add_int("OptionId") # stringvipgoodsname.xml
        add_int("Amount") # times per account
elif f == 4: # purchase completed
    add_int("OptionId")

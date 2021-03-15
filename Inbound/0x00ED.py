from script_api import *

f = AddByte("function")

if f == 0: # activate premium
    AddInt("UserObjectId")
    AddLong("Premium expiration")
elif f == 1: # daily rewards
    m = AddInt("flag?")
    if m != 0:
        m = AddInt("Unknown")
        while m != 1:
            m = AddInt("Unknown")
elif f == 2: # confirm reward claimed
    AddInt("RewardId")
elif f == 3: # purchase options
    count = AddInt("Count")
    for i in range(count):
        AddInt("OptionId") # stringvipgoodsname.xml
        AddInt("Amount") # times per account
elif f == 4: # purchase completed
    AddInt("OptionId")

from script_api import *

# RequestFieldEnter
# Request item use: 28 30 28 1F 73 95 70 26 07 00 32 00 30 00 30 00 30 00 31 00 31 00 34 00 (ItemUid / MapIdString)
f = AddByte("function")
if f == 1: # car taxi
    AddInt("MapId")
    AddInt("Unknown") # 100000000
elif f == 3: # rotor taxi
    AddInt("MapId")
elif f == 4: # rotor taxi (pay merets)
    AddInt("MapId")

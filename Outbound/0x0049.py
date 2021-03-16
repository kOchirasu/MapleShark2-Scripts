from script_api import *

# RequestFieldEnter
# Request item use: 28 30 28 1F 73 95 70 26 07 00 32 00 30 00 30 00 30 00 31 00 31 00 34 00 (ItemUid / MapIdString)
f = add_byte("function")
if f == 1: # car taxi
    add_int("MapId")
    add_int("Unknown") # 100000000
elif f == 3: # rotor taxi
    add_int("MapId")
elif f == 4: # rotor taxi (pay merets)
    add_int("MapId")

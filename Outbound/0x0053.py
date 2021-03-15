from script_api import *

AddUnicodeString("Name")
AddUnicodeString("Message")

f = AddByte("function")
if f == 0: # reporting player
    AddInt("Unknown") # 1
elif f == 1: # reporting chat
    AddInt("Unknown")
    AddUnicodeString("UnknownStr")
elif f == 2: # reporting poster
    AddInt("Unknown")
    AddLong("Unknown")
    AddUnicodeString("UnknownStr")
elif f == 3: # reporting design item
    AddInt("Unknown")
    AddLong("Unknown")
elif f == 4: # reporting real estate item (house)
    AddInt("Bit-flag of reasons")
    AddLong("PlayerId")
    AddInt("Unknown") # 0
    AddInt("Unknown") #0
elif f == 7: # reporting pet
    AddInt("Unknown")

"""
AddByte("Unknown")
AddByte("Unknown")
AddLong("Unknown")
AddLong("Unknown")
AddUnicodeString("UnknownStr")
AddUnicodeString("UnknownStr")
AddLong("Unknown")
AddString("UnknownStr")
AddUnicodeString("UnknownStr")
AddLong("Unknown")
AddLong("Unknown")
AddString("UnknownStr")
AddInt("Unknown")
AddLong("Unknown")
"""

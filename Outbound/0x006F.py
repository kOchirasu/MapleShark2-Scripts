from script_api import *

f = AddByte("Function")

if f == 0: # list party
    AddUnicodeString("PartyName")
    AddBool("IsPublic")
    AddInt("MaxMembers")
elif f == 1: # cancel listing
    pass # none
elif f == 2: # load listings
    AddInt("Unknown")
    AddInt("Unknown")
    AddByte("PartyType")
    AddUnicodeString("UnknownStr")
    AddInt("PageNumber")
    AddInt("Unknown")

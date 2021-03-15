from script_api import *

f = AddByte("function")

if f == 1: # smite
    AddUnicodeString("PlayerName")
elif f == 2: # kick
    AddUnicodeString("PlayerName")
elif f == 3: # revive
    AddUnicodeString("PlayerName")
elif f == 6: # save poral
    AddBool("false const")
    AddInt("CoordB")
    AddUnicodeString("PortalName")
    AddByte("MethodOfUse")
    AddByte("Destination")
    AddUnicodeString("DestinationStr") # PortalId/MapId/AccountId
elif f == 13: # manage portal
    AddInt("PortalId")

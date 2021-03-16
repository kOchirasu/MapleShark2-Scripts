from script_api import *

f = add_byte("function")

if f == 1: # smite
    add_unicode_str("PlayerName")
elif f == 2: # kick
    add_unicode_str("PlayerName")
elif f == 3: # revive
    add_unicode_str("PlayerName")
elif f == 6: # save poral
    add_bool("false const")
    add_int("CoordB")
    add_unicode_str("PortalName")
    add_byte("MethodOfUse")
    add_byte("Destination")
    add_unicode_str("DestinationStr") # PortalId/MapId/AccountId
elif f == 13: # manage portal
    add_int("PortalId")

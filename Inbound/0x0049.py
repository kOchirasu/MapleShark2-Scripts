''' FIELD_PORTAL '''
from script_api import *
from common import *

f = add_byte("Function")
add_int("PortalId")
if f == 0: # load portal
    add_bool("Visible")
    add_bool("Enabled")
    decode_coordF("Position")
    decode_coordF("Rotation")
    decode_coordF("PortalDimension")
    add_unicode_str("Model") # Eff_Com_Portal_E
    add_int("TargetMapId")
    add_int("ObjectId")
    add_int("Unknown")
    add_bool("MinimapVisible")
    add_long("UnknownLongId")
    add_byte("PortalType")
    add_int("StartTick")
    add_short("Unknown")
    add_int("EndTick")
    add_bool("Unknown") # locked?
    add_unicode_str("PortalOwnerName") # minigame portal
    add_unicode_str("UnknownStr")
    add_unicode_str("UnknownStr")
elif f == 1: # remove portal
    pass
elif f == 2: # trigger portal
    add_bool("Visible")
    add_bool("Enabled")
    add_bool("MinimapVisible")
    add_short("Unknown")
elif f == 3:
    decode_coordF("Position")
    decode_coordF("Rotation")

from script_api import *
from common import *

f = AddByte("Function")
AddInt("PortalId")
if f == 0: # load portal
    AddBool("Visible")
    AddBool("Enabled")
    DecodeCoordF("Position")
    DecodeCoordF("Rotation")
    DecodeCoordF("PortalDimension")
    AddUnicodeString("UnknownStr") # Eff_Com_Portal_E
    AddInt("TargetMapId")
    AddInt("ObjectId")
    AddInt("Unknown")
    AddBool("MinimapVisible")
    AddLong("UnknownLongId")
    AddByte("PortalType")
    AddInt("StartTick")
    AddShort("Unknown")
    AddInt("EndTick")
    AddBool("Unknown") # locked?
    AddUnicodeString("PortalOwnerName") # minigame portal
    AddUnicodeString("UnknownStr")
    AddUnicodeString("UnknownStr")
elif f == 1: # remove portal
    pass # ??
elif f == 2: # trigger portal
    AddBool("Visible")
    AddBool("Enabled")
    AddBool("MinimapVisible")
    AddShort("Unknown")
elif f == 3:
    DecodeCoordF("Location")
    DecodeCoordF("Rotation")

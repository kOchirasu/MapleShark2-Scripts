from script_api import *

f = AddByte("function")
if f == 6:
    AddBool("Disabled") # 0 Should NOT be disabled
    AddInt("CoordB")
    AddUnicodeString("PortalName")
    AddByte("MethodOfUse")
    AddByte("Destination")
    AddUnicodeString("UnknownStr")
    count = AddInt("count")
    for i in range(count):
        AddUnicodeString("OtherPortalName")

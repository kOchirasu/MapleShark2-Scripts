from script_api import *

f = add_byte("function")
if f == 6:
    add_bool("Disabled") # 0 Should NOT be disabled
    add_int("CoordB")
    add_unicode_str("PortalName")
    add_byte("MethodOfUse")
    add_byte("Destination")
    add_unicode_str("UnknownStr")
    count = add_int("count")
    for i in range(count):
        add_unicode_str("OtherPortalName")

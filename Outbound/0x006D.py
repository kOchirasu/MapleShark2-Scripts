from script_api import *

f = add_byte("Function")
if f == 0:
    add_int("CurrentMapId")
    add_int("PortalId")
    add_int("unknown")
    add_int("unknown")
    add_unicode_str("unknown")
    add_unicode_str("Password") # For locked portals
elif f == 1:
    pass
elif f == 2:
    add_int("unknown")
    add_int("unknown")
    add_int("unknown")
    add_long("unknown")
    add_unicode_str("unknown")
elif f == 3:
    pass
elif f == 4:
    pass
elif f == 5:
    pass
elif f == 6:
    pass

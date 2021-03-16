from script_api import *

f = add_byte("Function")
if f == 0:
    add_int("CurrentMapId")
    add_int("PortalId")
    add_field("Unknown", 10)
    add_unicode_str("Password") # For locked portals

from script_api import *

f = add_byte("Function")

if f == 0: # list party
    add_unicode_str("PartyName")
    add_bool("IsPublic")
    add_int("MaxMembers")
elif f == 1: # cancel listing
    pass # none
elif f == 2: # load listings
    add_int("Unknown")
    add_int("Unknown")
    add_byte("PartyType")
    add_unicode_str("UnknownStr")
    add_int("PageNumber")
    add_int("Unknown")

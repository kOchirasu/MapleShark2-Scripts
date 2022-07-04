from script_api import *

f = add_byte("Function")

if f == 0: # Summon
    add_long("Pet uid")
elif f == 1: # Remove Summon
    add_long("Pet uid")
elif f == 3: # replace
    add_long("Pet uid")
elif f == 4: # rename
    add_unicode_str("New name")
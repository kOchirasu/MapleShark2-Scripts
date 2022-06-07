''' REQUEST_HOME '''
from script_api import *

f = add_byte("function")
if f == 0: # Accept invite to home
    add_unicode_str("Unknown")
    add_byte("Unknown")
elif f == 1: # Invite to home
    add_unicode_str("Unknown")
elif f == 3: # Creating new home
    add_int("HomeType") # -1 = none

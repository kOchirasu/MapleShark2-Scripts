''' PATCH_FILE '''
from script_api import *

f = add_byte("mode")
if f == 1: # delete?
    pass
elif f == 2:
    pass
elif f == 3: # download online?
    count = add_int("count")
    for i in range(count):
        add_str("unknown")
        add_long("unknown")
        add_str("unknown")
elif f == 5: # download from packet?
    add_str("unknown")
    add_long("unknown")
    size = add_int("unknown")
    add_byte("unknown")
    add_field("buffer", size)
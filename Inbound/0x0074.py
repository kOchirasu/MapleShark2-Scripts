''' RELOCATE_WORLD '''
from script_api import *

f = add_byte("function")
if f == 0:
    count = add_int("count")
    for i in range(count):
        add_int("unknown")
        add_unicode_str("unknown")
elif f == 2:
    n = add_int("unknown")
    if n == 0:
        pass # s_relocate_world_err+MsgBox
    else:
        add_unicode_str("unknown")
        add_short("unknown")
        add_int("unknown")
        # throw exception(0x80070057) "The parameter is incorrect"
elif f == 4:
    pass
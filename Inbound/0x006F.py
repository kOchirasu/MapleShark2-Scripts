''' GVG '''
from script_api import *

count = add_int("count")
for i in range(count):
    f = add_int("function")
    if f == 1:
        add_bool("unknown")
    elif f == 7: # CContentShutdownManager
        count = add_short("count")
        for j in range(count):
            add_short("unknown")
    elif f == 25:
        add_int("unknown")
        add_int("unknown")
        add_int("unknown")
        add_int("unknown")
    elif f == 34:
        add_short("unknown")
        add_int("unknown")
        add_int("unknown")
    elif f == 42:
        add_float("unknown")
        add_float("unknown")
    elif f == 43: # CReconnectionManager
        pass
    else:
        pass # Unknown GVGroupType

''' BREAKABLE '''
from script_api import *

f = add_bool("function")
if f == 1:
    count = 1
else:
    count = add_int("count")

for i in range(count):
    with Node("Breakable " + str(i), True):
        add_str("EntityId")
        add_byte("State") # 2,3,4,5,6
        add_bool("IsVisible")
        add_int("DurationTick")
        add_int("SpawnTick")

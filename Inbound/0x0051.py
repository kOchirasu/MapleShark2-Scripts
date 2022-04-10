''' ROOM_TIMER '''
from script_api import *

f = add_byte("function")
if f == 0: # UIPopUpMenu
    type = add_byte("type")
    if type == 1:
        pass # UITimerDialog
    else:
        pass # UITimerGaugeDialog
    add_int("ServerTick")
    add_int("Duration (ms)")
    add_int("Unknown")
elif f == 1: # Change time
    add_int("Unknown")
    add_int("Unknown")
    type = add_int("type")
    delta = add_int("TimeDelta")
    if type == 1:
        if delta < 0:
            pass # s_room_decrease_time
        elif delta > 0:
            pass # s_room_increase_time
    else:
        pass # s_room_increase_time_type2
elif f == 2:
    type = add_byte("type")
    if type == 1:
        pass # UITimerDialog
    else:
        pass # UITimerGaugeDialog
    add_int("ServerTick")
    add_int("Duration (ms)")
    add_int("Unknown")
elif f == 3: # unknown
    pass
elif f == 4: # resets values to 0
    pass
elif f == 5: # resets values to 0
    pass

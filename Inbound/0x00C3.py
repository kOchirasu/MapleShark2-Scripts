from script_api import *

f = add_byte("Function")

if f == 0: # open portal?
    add_int("PortalId") # 80005
    add_int("Unknown") # 39
    add_unicode_str("Unknown") # s_massive_event_message
    add_unicode_str("Unknown") # System_Quiz_Global_Portal
    add_unicode_str("Unknown") # s_massive_event_name_red_arena
    add_unicode_str("Unknown") # s_massive_event_name_spring_beach
    add_unicode_str("Unknown") # s_massive_event_name_crazy_runner
elif f == 1: # close portal?
    add_int("PortalId") # 80005
elif f == 3: # something append message
    pass
elif f == 4: # something append message
    pass

from script_api import *

# Request 0x0025 08 (SendJob)
f = add_byte("Function")
if f == 7:
    add_int("Unknown")
    add_long("Unknown")
    add_int("Unknown")
    add_short("Unknown")
elif f == 8:
    # SendJob load
    pass
elif f == 9 or f == 11:
    count = add_int("Count")
    for i in range(count):
        start_node("Skill " + str(i))
        add_int("SkillId")
        add_short("Skill Points")
        b = add_bool("Enabled")
        end_node(b)
elif f == 10: # Reset skillbook
    add_int("Unknown") # 0 = basic, 1 = awakening, 2 = both

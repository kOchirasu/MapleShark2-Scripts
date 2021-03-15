from script_api import *

# Request 0x0025 08 (SendJob)
f = AddByte("Function")
if f == 8:
    # SendJob load
    pass
elif f == 9 or f == 11:
    count = AddInt("Count")
    for i in range(count):
        StartNode("Skill " + str(i))
        AddInt("SkillId")
        AddShort("Skill Points")
        b = AddBool("Enabled")
        EndNode(b)
elif f == 10: # Reset skillbook
    AddInt("Unknown") # 0 = basic, 1 = awakening, 2 = both

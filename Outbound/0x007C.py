from script_api import *

f = AddByte("function")

if f == 0: # open dialog
    pass # none
elif f == 1: # update macro settings
    count = AddInt("count")
    for i in range(count):
        with Node("Macro " + str(i), True):
            AddUnicodeString("MacroName")
            AddLong("KeyId") # 700001, 700002, 700003
            skillCount = AddInt("skillCount")
            for j in range(skillCount):
                AddInt("SkillId")

from script_api import *

f = AddByte("function")

# 0 = Save Macro Response
# 2 = Load Macro (At Login)
if f == 0 or f == 2 :
    count = AddInt("count")
    for i in range(count):
        with Node("Macro " + str(i), True):
            AddUnicodeString("MacroName")
            AddLong("KeyId") # 700001, 700002, 700003
            skillCount = AddInt("skillCount")
            for j in range(skillCount):
                AddInt("SkillId")

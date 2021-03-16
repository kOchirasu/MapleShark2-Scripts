from script_api import *

f = add_byte("function")

if f == 0: # open dialog
    pass # none
elif f == 1: # update macro settings
    count = add_int("count")
    for i in range(count):
        with Node("Macro " + str(i), True):
            add_unicode_str("MacroName")
            add_long("KeyId") # 700001, 700002, 700003
            skillCount = add_int("skillCount")
            for j in range(skillCount):
                add_int("SkillId")

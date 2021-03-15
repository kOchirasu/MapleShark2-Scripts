from script_api import *

f = AddByte("function")
if f == 0:
    # LoadSkills
    pass
elif f == 1: # SaveSkills
    AddLong("ActiveSkillTabId")
    AddLong("SavingTabId") # 0 = not saving any tab
    AddInt("SkillRank")
    count = AddInt("SkillTabsCount")
    for i in range(count):
        with Node("SkillTab " + str(i), True):
            AddLong("SkillTabId")
            AddUnicodeString("SkillTabName")
            skillCount = AddInt("count")
            for j in range(skillCount):
                AddInt("SkillId")
                AddInt("SkillPoints")
elif f == 2:
    # Rename skill tab
    AddLong("SkillTabId")
    AddUnicodeString("SkillTabName")

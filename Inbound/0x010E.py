from script_api import *

f = AddByte("function")
if f == 0:
    AddInt("SkillRank")
    AddLong("ActiveSkillTabId")
    count = AddInt("SkillTabsCount")
    for i in range(count):
        with Node("SkillTab " + str(i), True):
            AddLong("SkillTabId")
            AddUnicodeString("SkillTabName")
            skillCount = AddInt("count")
            for j in range(skillCount):
                AddInt("SkillId")
                AddInt("SkillPoints")
elif f == 1:
    AddLong("SavedSkillTabId")
    AddLong("SavingTabId") # TabId to save
    AddInt("SkillRank")
elif f == 2:
    # Change skill tab name response
    AddLong("SkillTabId")
    AddUnicodeString("SkillTabName")
    AddByte("Unknown")

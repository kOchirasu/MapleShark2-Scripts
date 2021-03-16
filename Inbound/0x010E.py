from script_api import *

f = add_byte("function")
if f == 0:
    add_int("SkillRank")
    add_long("ActiveSkillTabId")
    count = add_int("SkillTabsCount")
    for i in range(count):
        with Node("SkillTab " + str(i), True):
            add_long("SkillTabId")
            add_unicode_str("SkillTabName")
            skillCount = add_int("count")
            for j in range(skillCount):
                add_int("SkillId")
                add_int("SkillPoints")
elif f == 1:
    add_long("SavedSkillTabId")
    add_long("SavingTabId") # TabId to save
    add_int("SkillRank")
elif f == 2:
    # Change skill tab name response
    add_long("SkillTabId")
    add_unicode_str("SkillTabName")
    add_byte("Unknown")

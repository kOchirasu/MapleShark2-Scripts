from script_api import *

f = add_byte("function")
if f == 0:
    # LoadSkills
    pass
elif f == 1: # SaveSkills
    add_long("ActiveSkillTabId")
    add_long("SavingTabId") # 0 = not saving any tab
    add_int("SkillRank")
    count = add_int("SkillTabsCount")
    for i in range(count):
        with Node("SkillTab " + str(i), True):
            add_long("SkillTabId")
            add_unicode_str("SkillTabName")
            skillCount = add_int("count")
            for j in range(skillCount):
                add_int("SkillId")
                add_int("SkillPoints")
elif f == 2:
    # Rename skill tab
    add_long("SkillTabId")
    add_unicode_str("SkillTabName")
elif f == 4: # Add skill tab
    add_int("const") # 20272
    add_bool("unknown")

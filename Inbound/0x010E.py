''' SKILL_BOOK_TREE '''
from script_api import *

def decode_skill_tab():
    add_long("SkillTabId")
    add_unicode_str("SkillTabName")
    skillCount = add_int("count")
    for j in range(skillCount):
        add_int("SkillId")
        add_int("SkillPoints")

f = add_byte("function")
if f == 0:
    add_int("MaxTabs")
    add_long("ActiveSkillTabId")
    count = add_int("SkillTabsCount")
    for i in range(count):
        with Node("SkillTab " + str(i), True):
            decode_skill_tab()
elif f == 1:
    add_long("ActiveSkillTabId")
    add_long("SavingTabId") # TabId to save
    add_int("SkillRank")
elif f == 2:
    # Change skill tab name response
    add_long("SkillTabId")
    add_unicode_str("SkillTabName")
    add_bool("Error") # true -> s_ban_check_err_any_word
elif f == 4:
    add_int("MaxTabs")
    # s_skillbook_tree_config_payment_sucess
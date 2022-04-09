''' SKILL_COOLDOWN '''
from script_api import *

count = add_byte("Count")
for i in range(count):
    add_long("SkillId")
    add_int("EndTick") # 0 if no cooldown
    add_int("Unknown")

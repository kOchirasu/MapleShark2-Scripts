''' FIELD_ADD_NPC '''
from script_api import *
from common import *
from stats import *

add_int("ObjectId")
add_int("NpcId")
decode_coordF("Position")
decode_coordF("Rotation")

# if (not friendly and class >= 3)
'''
add_str("npcstring")
'''

# If valid NpcId
decode_npc_stats()

add_bool("IsDead")
count = add_short("Count")
for i in range(count):
    with Node("buff " + str(i)):
        add_int("TargetObjectId")
        add_int("BuffObjectId")
        add_int("OwnerObjectId")
        decode_additional_effect1()
        decode_additional_effect2()

add_long("ItemUid") # From PetNpc
add_byte("CNpc+18F0")
add_int("NpcLevel") # technically level is a short, so this is just padded with "00 00"
add_int("CNpc+1928")

# if (not friendly and class >= 3)
'''
add_unicode_str("effect string")
count = add_int("Count")
for i in range(count):
    add_int("SkillId")
    add_short("SkillLevel")
add_int("CNpc+197C")
'''

# if (Npc has hiddenhpadd)
'''
add_long("HiddenHpAdd")
'''

add_bool("Npc+1988")

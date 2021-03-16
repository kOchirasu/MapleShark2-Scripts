from script_api import *
from common import *

add_int("ObjectId")
decode_player()
decode_skill_tree()
decode_coordF("")
decode_coordF("")
add_byte("Unknown+473")
with Node("Stats"):
    count = add_byte("StatsCount")
    if count == 35:
        for i in range(3):
            add_long("Health")
            add_int("AttackSpeed")
            add_int("MovementSpeed")
            add_int("MountMovementSpeed")
            add_int("JumpHeight")
    else:
        for i in range(count):
            statType = add_byte("StatType")
            for j in range(3):
                if statType == 4: # Use long for HP
                    add_long("HP")
                else:
                    add_int("StatType:" + str(statType))

add_byte("Unknown+475")
add_byte("Unknown+476")
add_int("Unknown+477")
add_long("Unknown+481")
add_long("Unknown+489")
with Node("UgcNode"):
    flag = add_bool("Flag")
    if flag:
        decode_ugc_data()

add_int("Unknown+498")
decode_skin_color()

add_unicode_str("Profile Url")
with Node("Mount"):
    flag = add_bool("IsOnMount")
    if flag:
        add_byte("Unknown") # 1
        add_int("MountId")
        add_int("MountObjectId")
        add_byte("Unknown") # ??

add_int("Unknown+513")
add_long("Timestamp")
add_int("Weekly Architect Score")
add_int("Architect Score")

flag = add_bool("Flag")
if flag:
    with Node("Buffer 1"):
        size = add_int("BufferSize")
        add_field("Buffer", size)
    add_byte("Separator?")
    with Node("Buffer 2"):
        size = add_int("BufferSize")
        add_field("Buffer", size)
    add_byte("Separator?")
    with Node("Buffer 3"):
        size = add_int("BufferSize")
        add_field("Buffer", size)

    with Node("add_itionalEffects"):
        count = add_short("Count")
        for i in range(count):
            with Node("Passive buff " + str(i), True):
                add_int("UserObjectId")
                add_int("Unknown+778")
                add_int("UserObjectId")
                decode_additional_effect()
                add_long("add_itionalEffect2")
    
    with Node("Node", True):
        add_int("SkillBookRelated1")
        add_int("SkillBookRelated2")
    
    add_byte("Unknown+860")
    with Node("Node", True):
        add_int("Unknown+861")
        add_byte("Unknown+865")
        add_byte("Unknown+866")
    
    add_int("TitleId")
    with Node("Node", True):
        add_short("Unknown+871")
        add_byte("Unknown+873")
    
    add_int("Unknown+874")
    b = add_bool("HasPet")
    if b:
        with Node("FieldPet"):
            id = add_int("PetItemId")
            add_long("PetUid")
            add_int("PetLevel")
            decode_item(id)
        
    add_long("PremiumExpirationTime")
    add_int("unknown -1") # 724497??
    add_byte("Unknown+891")
    add_int("Unknown+892")
    count = add_int("count")
    for i in range(count):
        add_int("Unknown")
        add_str("Unknown")
    add_short("Unknown+900")
else:
    add_int("Unknown")

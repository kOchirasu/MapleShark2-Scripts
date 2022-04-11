''' FIELD_ADD_USER '''
from script_api import *
from common import *

add_int("ObjectId")
decode_player()
decode_skill_tree()
decode_coordF("Position")
decode_coordF("Rotation")
add_byte("MyPC+154")
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

add_bool("InBattle")

with Node("gameObject_vtbl+572 virtual call"):
    add_byte("Unknown")
    with Node("CubeItemInfo"):
        add_int("unknown")
        add_long("unknown")
        add_long("unknown")
        isUgc = add_bool("isUgc")
        if isUgc:
            decode_ugc_data()

    add_int("Unknown")

decode_skin_color()

add_unicode_str("Profile Url")
with Node("Mount"):
    mode = add_byte("RideMode")
    add_int("MountId")
    add_int("MountObjectId")
    if mode == 0: # RideOnAction
        pass
    elif mode == 1: # RideOnActionUseItem
        add_int("ItemId")
        add_long("ItemUid")
        decode_ugc_data()
    elif mode == 2: # RideOnActionAdditionalEffect
        add_int("ItemId")
        add_short("unknown")
    elif mode == 3: # RideOnActionHideAndSeek
        pass

    count = add_byte("count")
    for i in range(count):
        add_int("unknown")
        add_byte("unknown")

add_int("MyPC+21AC")
add_long("Timestamp")
add_int("Weekly Architect Score")
add_int("Architect Score")

with Node("Equip Buffer"):
    add_bool("isDeflated")
    size = add_int("BufferSize")
    add_field("Buffer", size)

with Node("Skin2 Buffer"): # skins with stats
    add_bool("isDeflated")
    size = add_int("BufferSize")
    add_field("Buffer", size)

with Node("Badge Buffer"):
    add_bool("isDeflated")
    size = add_int("BufferSize")
    add_field("Buffer", size)

with Node("Buffs"):
    count = add_short("Count")
    for i in range(count):
        with Node("Buff " + str(i), True):
            add_int("TargetObjectId")
            add_int("AffectedObjectId")
            add_int("OwnerObjectId")
            decode_additional_effect1()
            decode_additional_effect2()

with Node("sub_BF6440", True):
    add_int("MyPC+2220")
    add_int("MyPC+2224")

add_byte("MyPC+2228")

with Node("sub_5F1C30", True):
    add_int("MyPC+C")
    add_byte("MyPC+10")
    add_byte("MyPC+24")

add_int("TitleId")
with Node("Insignia", True):
    add_short("InsigniaId")
    add_byte("InsigniaValue")

add_int("MyPC+1636")

b = add_bool("HasPet")
if b:
    with Node("FieldPet"):
        id = add_int("PetItemId")
        add_long("PetUid")
        add_int("PetLevel")
        decode_item(id)

add_long("PremiumExpirationTime")
add_int("MyPC+15F0") # -1, 724497??
add_byte("MyPC+15F4")
add_int("TailLength")  # MushkingRoyale tail effect kill count

# this data is stored in a hash map
count = add_int("count")
for i in range(count):
    add_int("Unknown")
    add_str("Unknown")

add_short("MyPC+2394")

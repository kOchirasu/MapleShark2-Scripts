from script_api import *
from common import *

AddInt("ObjectId")
DecodePlayer()
DecodeSkillTree()
DecodeCoordF("")
DecodeCoordF("")
AddByte("Unknown+473")
with Node("Stats"):
    count = AddByte("StatsCount")
    if count == 35:
        for i in range(3):
            AddLong("Health")
            AddInt("AttackSpeed")
            AddInt("MovementSpeed")
            AddInt("MountMovementSpeed")
            AddInt("JumpHeight")
    else:
        for i in range(count):
            statType = AddByte("StatType")
            for j in range(3):
                if statType == 4: # Use long for HP
                    AddLong("HP")
                else:
                    AddInt("StatType:" + str(statType))

AddByte("Unknown+475")
AddByte("Unknown+476")
AddInt("Unknown+477")
AddLong("Unknown+481")
AddLong("Unknown+489")
with Node("UgcNode"):
    flag = AddBool("Flag")
    if flag:
        DecodeUgcData()

AddInt("Unknown+498")
DecodeSkinColor()

AddUnicodeString("Profile Url")
with Node("Mount"):
    flag = AddBool("IsOnMount")
    if flag:
        AddByte("Unknown") # 1
        AddInt("MountId")
        AddInt("MountObjectId")
        AddByte("Unknown") # ??

AddInt("Unknown+513")
AddLong("Timestamp")
AddInt("Weekly Architect Score")
AddInt("Architect Score")

flag = AddBool("Flag")
if flag:
    with Node("Buffer 1"):
        size = AddInt("BufferSize")
        AddField("Buffer", size)
    AddByte("Separator?")
    with Node("Buffer 2"):
        size = AddInt("BufferSize")
        AddField("Buffer", size)
    AddByte("Separator?")
    with Node("Buffer 3"):
        size = AddInt("BufferSize")
        AddField("Buffer", size)

    with Node("AdditionalEffects"):
        count = AddShort("Count")
        for i in range(count):
            with Node("Passive buff " + str(i), True):
                AddInt("UserObjectId")
                AddInt("Unknown+778")
                AddInt("UserObjectId")
                DecodeAdditionalEffect()
                AddLong("AdditionalEffect2")
    
    with Node("Node", True):
        AddInt("SkillBookRelated1")
        AddInt("SkillBookRelated2")
    
    AddByte("Unknown+860")
    with Node("Node", True):
        AddInt("Unknown+861")
        AddByte("Unknown+865")
        AddByte("Unknown+866")
    
    AddInt("TitleId")
    with Node("Node", True):
        AddShort("Unknown+871")
        AddByte("Unknown+873")
    
    AddInt("Unknown+874")
    b = AddBool("HasPet")
    if b:
        with Node("FieldPet"):
            id = AddInt("PetItemId")
            AddLong("PetUid")
            AddInt("PetLevel")
            DecodeItem(id)
        
    AddLong("PremiumExpirationTime")
    AddInt("unknown -1") # 724497??
    AddByte("Unknown+891")
    AddInt("Unknown+892")
    count = AddInt("count")
    for i in range(count):
        AddInt("Unknown")
        AddString("Unknown")
    AddShort("Unknown+900")
else:
    AddInt("Unknown")

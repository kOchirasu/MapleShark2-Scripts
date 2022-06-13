''' NPC_TALK '''
from script_api import *

f = add_byte("Function")
if f == 0: # Close
    pass
elif f == 1: # Start Talking
    add_int("ObjectId?")
elif f == 2: # Continue Talking
    add_int("index")
elif f == 4: # Enchant related
    mode = add_short("unknown")
    if mode == 1:
        add_long("ItemUid")
elif f == 6: # Enchant
    add_int("NpcId")
    add_int("EnchantMasterScriptID")
    mode = add_short("1") # same as 4
    # 1 = PutItem
    # 2 = BeginEnchant
    # 3 = FinishEnchant
    if mode == 1:
        add_long("ItemUid")
elif f == 7: # Quest
    add_int("QuestId")
    add_short("unknown") # 2 or 0
    # QuestPacket(4, CompleteQuest) => 0
    # QuestPacket(2, StartQuest) => 2
elif f == 8: # AllianceQuest, onAccept
    add_int("QuestId")
    add_short("Unknown") # 2 or 0
elif f == 9: # AllianceQuest, onTalk
    pass
elif f == 11: # CCustomSelectableDistractorCinematicComponent, similar to 2
    add_int("objectId")
    add_int("index")

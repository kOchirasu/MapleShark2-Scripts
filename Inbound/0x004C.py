''' NPC_TALK (NOTE: this one is too complicated to get accurate) '''
from script_api import *
from common import *

# distractor (this is a guess)
def decode_script_content():
    add_unicode_str("text")
    add_unicode_str("goto") # As ASCII
    add_unicode_str("gotoFail") # As ASCII

def decode_cinematic_content():
    decode_script_content()
    add_int("Unknown")
    b = add_bool("Unknown")
    if b:
        count = add_byte("count")
        for i in range(count):
            # NOTE: this is not actually the same funciton, but struct looks the same
            decode_script_content()

def decode_npc_dialog():
    add_int("ScriptId")
    add_int("ScriptIndex") # when there's mutliple parts to a scriptId
    add_int("Options") # Affects selections...

def decode_talk_script():
    add_int("NpcId")
    add_byte("Unknown")
    add_int("Unknown")
    add_bool("RandomPick")
    count = add_int("count")
    for i in range(count):
        t = add_byte("ScriptType")
        if t == 0: # CCinematicContent
            decode_cinematic_content()
        elif t == 1: # CChatBalloonContent
            decode_script_content()
        else: # I think client will crash in this case?
            raise Exception()

f = add_byte("Function")
if f == 0: # EndTalk
    pass
elif f == 1:
    add_int("ObjectId")
    add_byte("flags")
    decode_npc_dialog()
elif f == 2: # continue talking
    add_byte("flags")
    add_int("ObjectId")
    decode_npc_dialog()
elif f == 8:
    add_byte("flags")
    add_int("ObjectId")
    decode_npc_dialog()
    # sub_E2AF00
elif f == 3: # action
    f = add_byte("Function")
    if f == 1:
        add_unicode_str("UnknownStr")
    elif f == 3: # MoveMyPC
        add_int("PortalId")
    elif f == 4: # Gamble
        add_unicode_str("UnknownStr") # BeautyShopDialog
        add_unicode_str("UnknownStr") # itemcolor
    elif f == 5: # ItemReward
        count = add_int("count")
        for i in range(count):
            id = add_int("ItemId")
            add_byte("rarity")
            add_int("amount")
            decode_item(id)
    elif f == 6: # RewardNotify (Exp)
        add_long("Exp")
    elif f == 7: # RewardNotify
        add_long("field_64")
    elif f == 8: # adds this value to dialog option
        add_int("AddOption")
    elif f == 9:
        add_int("Add_field_74")
        add_bool("Set_field_78")
    elif f == 10: # CutsceneMovie
        add_int("Unknown")
        add_unicode_str("Unknown")
elif f == 4:
    decode_script_content()
elif f == 9:
    add_byte("flag")
    decode_npc_dialog()
    # sub_E2AF00
elif f == 10:
    add_int("ObjectId")
    add_short("Unknown") # should be 1
    decode_talk_script()

''' Flag handling
bit flags: 1 | 2 | 4 | 8 | 16
1=
2=
4=Quest
8=sub_649B00
16=Cinematic (This is required for dialog options, f == 2 only?)
'''
from re import T
from script_api import *
from common import *

f = add_byte("Function")
if f == 0: # Start (broadcast)
    t = add_short("type")
    add_int("ObjectId")
    add_long("CharacterId")
    decode_coordF("Position")
    decode_coordF("Rotation?")
    if t == 0: # CConstructionGuideObject
        add_long("Unknown")
    elif t == 1: # CFishingGuideObject
        pass
    elif t == 3 : # CSkillMagicControlGuide
        add_long("Unknown")
        add_int("Unknown")
        add_short("Unknown")
        add_byte("Unknown")
        add_byte("Unknown")
        add_int("Unknown")
        count = add_byte("count")
        for i in range(count):
            add_long("unknown") # CTargetRecord
            add_byte("unknown") # not sure
elif f == 1: # End (broadcast)
    add_int("GuideObjectId")
    add_long("CharacterId")
elif f == 2: #sync (broadcast others)
    add_int("GuideObjectId")
    count = add_byte("segments")
    for i in range(count):
        decode_state_sync()

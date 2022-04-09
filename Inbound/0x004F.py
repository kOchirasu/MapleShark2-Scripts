from script_api import *
from common import *

def decode_trigger_sync():
    id = add_int("SomeTriggerId")
    if id < 5000:
        start_node("TriggerMesh")
        add_bool("UnknownBool")
        add_byte("UnknownByte")
        add_int("UnknownInt")
        add_unicode_str("UnknownStr")
        add_float("UnknownFloat")
    else:
        start_node("TriggerEffect")
        add_bool("UnknownBool")
        add_byte("UnknownByte")
        add_int("UnknownInt")
    # Actor
    # Byte
    # UnicodeString

    # Rope
    # Bool
    # Bool
    # Int

    # Cube/Sound
    # Bool
    end_node(False)


# Guild
f = add_byte("Function")
if f == 0:
    add_field("AddTrigger")
elif f == 1:
    add_field("RemoveTrigger")
elif f == 2:
    count = add_int("count")
    for i in range(count):
        decode_trigger_sync()
elif f == 3:
    decode_trigger_sync()
elif f == 5: # camera path
    count = add_byte("count")
    for i in range(count):
        add_int("CameraPathId")
    add_byte("Unknown")
elif f == 6:
    pass # none (0.0)
elif f == 8: # display some notice ui
    n = add_byte("Unknown")
    with Node("type " + str(n), True):
        if n == 1: # GuideManager(21)
            add_int("Unknown")
        elif n == 2: # UIGuideEvent
            add_int("EntityID")
            add_int("textID")
            add_int("durationTime")
        elif n == 3: # UIGuideEvent
            add_int("Unknown")
        elif n == 4: # UICutSceneMovie (Start)
            add_str("fileName")
            add_int("movieID")
        elif n == 5: # UICutSceneMovie (Skip)
            add_int("Unknown")
        elif n == 7: # StateTriggerEmotionData
            count = add_int("count")
            for i in range(count):
                add_unicode_str("UnknownStr")
        elif n == 8: # StateTriggerEmotionData
            add_byte("Unknown")
            add_int("Unknown")
            add_unicode_str("UnknownStr")
        elif n == 9: # TextureAnimation
            add_int("Unknown")
            add_unicode_str("UnknownStr")
        elif n == 10:
            decode_coordS("Unknown")
            add_bool("Unknown")
        elif n == 11:
            decode_coordS("Unknown")
            add_bool("Unknown")
        elif n == 12: # UI: TypingGameDialog
            add_int("Unknown")
            add_int("Unknown")
        # f(n)...
elif f == 11: # load script computer
    add_str("UnknownStr") # script xml
    # <?xml version="1.0" encoding="utf-8"?><ms2><state name="NewState1" posX="0" posY="0" /></ms2>
    # FileBuffer
    # TriggerEditorDialog
elif f == 14:
    f2 = add_byte("sub-function")
    if f2 == 1: # UI: TriggerTimerDialog (150)
        add_int("ServerTick")
        add_int("TimeMS")
        add_byte("arg4")
        add_int("arg5")
        add_unicode_str("arg6")
        #add_int("Unknown")
        #add_int("Unknown")
    elif f2 == 2: # UI: PvpObserverDialog (151)
        add_int("Unknown")
        add_int("Unknown")
        add_byte("Unknown")
    elif f2 == 5: # Same as 2
        add_int("Unknown")
        add_int("Unknown")
        add_byte("Unknown")
    elif f2 == 3: # UI Unknown (154, 155)
        add_int("Unknown")
        add_int("Unknown")
        add_byte("Unknown")
    elif f2 == 4: # UI Unknown (150 - TimerDialog, 212)
        add_int("Unknown")
        add_int("Unknown")
        add_byte("Unknown")
elif f == 15:
    pass # none
elif f == 16: # GameObjectEffectNifCtx (AddEffectNif)
    add_int("objectId")
    add_str("nifPath")
    add_bool("isOutline")
    add_float("scale")
    add_float("rotateZ")
elif f == 17: # (RemoveEffectNif)
    add_int("objectId") # objectId
elif f == 18: # side pop-up (SideNpcTalk)
    add_byte("type") # 1 = talk, 2  = cutin
    add_int("duration")
    add_str("UnknownStr")
    add_str("illustration")
    add_str("sound")
    add_str("UnknownStr")
    add_unicode_str("script")
elif f == 19:
    add_byte("Unknown")
    add_str("UnknownStr")
elif f == 20: # UI: NpcDualHpBarDialog (61, 101)
    b = add_bool("Visible")
    if b:
        add_int("ObjectId")
        add_int("durationTick")
        add_int("npcHpStep")
elif f == 21:
    add_int("Unknown")
elif f == 22:
    count = add_int("count")
    for i in range(count):
        add_int("PlayerObjectId")
    # additional/Etc/Eff_Target_Select_Keep.xml
    add_unicode_str("TargetEffect")
elif f == 23:
    count = add_int("count")
    for i in range(count):
        add_int("PlayerObjectId")
    # additional/Etc/Eff_Target_Select_Keep.xml
    add_unicode_str("TargetEffect")
elif f == 24: # remove above effects?
    pass # none

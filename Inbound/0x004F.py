''' TRIGGER '''
from script_api import *
from common import *

def decode_trigger_object():
    id = add_int("SomeTriggerId")
    add_bool("IsVisible")
    # These are just here as a baseline, see comments below for actual structs
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
    '''TriggerObject'''

    '''TriggerObjectSound'''

    '''TriggerObjectMesh
    add_bool("MinimapVisible")
    add_int("unknown")
    add_unicode_str("unknown)
    add_float("scale?")
    '''

    '''TriggerObjectActor
    add_unicode_str("unknown)
    '''

    '''TriggerObjectRope
    add_bool("unknown") # false
    add_int("unknown")
    '''

    '''TriggerObjectEffect
    add_bool("unknown")
    add_int("unknown")
    '''

    '''TriggerObjectCube'''

    '''TriggerObjectCamera'''
    end_node(False)


# Guild
f = add_byte("Function")
if f == 2: # load
    count = add_int("count")
    for i in range(count):
        decode_trigger_object()
elif f == 3: # update
    decode_trigger_object()
elif f == 5: # camera path
    count = add_byte("count")
    for i in range(count):
        add_int("CameraPathId")
    add_bool("Unknown")
elif f == 6: # camera related, end path?
    pass # none (0.0)
elif f == 8: # display some notice ui
    n = add_byte("Unknown")
    with Node("type " + str(n), True):
        if n == 1: # GuideManager(21 - Design)
            add_int("Unknown")
        elif n == 2: # UIGuideEvent - showSummary
            add_int("EntityID")
            add_int("textID")
            add_int("durationTime")
        elif n == 3: # UIGuideEvent - hideSummary
            add_int("Unknown")
        elif n == 4: # UICutSceneMovie (Start)
            add_str("fileName")
            add_int("movieID")
        elif n == 5: # UICutSceneMovie (Skip)
            add_int("movieID")
        elif n == 7: # StateTriggerEmotionData
            count = add_int("count")
            for i in range(count):
                add_unicode_str("UnknownStr")
        elif n == 8: # StateTriggerEmotionData
            add_byte("Unknown")
            add_int("Unknown")
            add_unicode_str("UnknownStr")
        elif n == 9: # TextureAnimation
            add_int("ObjectId")
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
elif f == 11: # load script computer
    add_str("UnknownStr") # script xml
    # <?xml version="1.0" encoding="utf-8"?><ms2><state name="NewState1" posX="0" posY="0" /></ms2>
    # FileBuffer
    # TriggerEditorDialog
elif f == 14: # timer related
    f2 = add_byte("sub-function")
    if f2 == 1: # UITriggerTimerDialog
        add_int("ServerTick")
        add_int("Duration")
        add_byte("arg4")
        add_int("arg5")
        add_unicode_str("arg6")
        #add_int("Unknown")
        #add_int("Unknown")
    elif f2 == 2: # UIPvPObserverDialog
        add_int("Unknown")
        add_int("Unknown")
        add_byte("Unknown")
    elif f2 == 5: # UIPvPObserverDialog, Similar to 2
        add_int("Unknown")
        add_int("Unknown")
        add_byte("Unknown")
    elif f2 == 3: # UIFreeForAllTimerDialog, UIPvPRankingDialog
        add_int("Unknown")
        add_int("Unknown")
        add_byte("Unknown")
    elif f2 == 4: # UITriggerTimerDialog, UIPvPTeamScoreDialog
        add_int("Unknown")
        add_int("Unknown")
        add_byte("Unknown")
elif f == 15:
    count = add_int("count")
    for i in range(count):
        add_int("unknown")
elif f == 16: # GameObjectEffectNifCtx (AddEffectNif)
    add_int("objectId")
    add_str("nifPath")
    add_bool("isOutline")
    add_float("scale")
    add_float("rotateZ")
elif f == 17: # (RemoveEffectNif)
    add_int("objectId") # objectId of field player
elif f == 18: # side pop-up (SidePopupTalkParam)
    add_byte("type") # 1 = talk, 2 = cutin
    add_int("duration")
    add_str("UnknownStr")
    add_str("illustration")
    add_str("sound")
    add_str("UnknownStr")
    add_unicode_str("script")
elif f == 19:
    add_byte("Unknown")
    add_str("UnknownStr") # comma delimited
elif f == 20: # UINpcDuelHPBarDialog
    b = add_bool("Visible")
    if b:
        add_int("ObjectId")
        add_int("durationTick")
        add_int("npcHpStep")
elif f == 21:
    u = add_int("Unknown")
    if u == 0:
        pass # s_user_trigger_msg_rollback
elif f == 22 or f == 23 or f == 24:
    count = add_int("count")
    for i in range(count):
        add_int("PlayerObjectId")
    # additional/Etc/Eff_Target_Select_Keep.xml
    add_unicode_str("TargetEffect")

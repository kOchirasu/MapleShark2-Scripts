from script_api import *
from common import *

def DecodeTriggerSync():
    id = AddInt("SomeTriggerId")
    if id < 5000:
        StartNode("TriggerMesh")
        AddBool("UnknownBool")
        AddByte("UnknownByte")
        AddInt("UnknownInt")
        AddUnicodeString("UnknownStr")
        AddFloat("UnknownFloat")
    else:
        StartNode("TriggerEffect")
        AddBool("UnknownBool")
        AddByte("UnknownByte")
        AddInt("UnknownInt")
    # Actor
    # Byte
    # UnicodeString

    # Rope
    # Bool
    # Bool
    # Int

    # Cube/Sound
    # Bool
    EndNode(False)


# Guild
f = AddByte("Function")
if f == 0:
    AddField("AddTrigger")
elif f == 1:
    AddField("RemoveTrigger")
elif f == 2:
    count = AddInt("count")
    for i in range(count):
        DecodeTriggerSync()
elif f == 3:
    DecodeTriggerSync()
elif f == 5: # camera path
    count = AddByte("count")
    for i in range(count):
        AddInt("CameraPathId")
    AddByte("Unknown")
elif f == 6:
    pass # none (0.0)
elif f == 8: # display some notice ui
    n = AddByte("Unknown")
    with Node("type " + str(n), True):
        if n == 1: # GuideManager(21)
            AddInt("Unknown")
        elif n == 2: # UIGuideEvent
            AddInt("EntityID")
            AddInt("textID")
            AddInt("durationTime")
        elif n == 3: # UIGuideEvent
            AddInt("Unknown")
        elif n == 4: # UICutSceneMovie (Start)
            AddString("fileName")
            AddInt("movieID")
        elif n == 5: # UICutSceneMovie (Skip)
            AddInt("Unknown")
        elif n == 7: # StateTriggerEmotionData
            count = AddInt("count")
            for i in range(count):
                AddUnicodeString("UnknownStr")
        elif n == 8: # StateTriggerEmotionData
            AddByte("Unknown")
            AddInt("Unknown")
            AddUnicodeString("UnknownStr")
        elif n == 9: # TextureAnimation
            AddInt("Unknown")
            AddUnicodeString("UnknownStr")
        elif n == 10:
            DecodeCoordS("Unknown")
            AddBool("Unknown")
        elif n == 11:
            DecodeCoordS("Unknown")
            AddBool("Unknown")
        elif n == 12: # UI: TypingGameDialog
            AddInt("Unknown")
            AddInt("Unknown")
        # f(n)...
elif f == 11: # load script computer
    AddString("UnknownStr") # script xml
    # <?xml version="1.0" encoding="utf-8"?><ms2><state name="NewState1" posX="0" posY="0" /></ms2>
    # FileBuffer
    # TriggerEditorDialog
elif f == 14:
    f2 = AddByte("sub-function")
    if f2 == 1: # UI: TriggerTimerDialog (150)
        AddInt("ServerTick")
        AddInt("TimeMS")
        AddByte("arg4")
        AddInt("arg5")
        AddUnicodeString("arg6")
        #AddInt("Unknown")
        #AddInt("Unknown")
    elif f2 == 2: # UI: PvpObserverDialog (151)
        AddInt("Unknown")
        AddInt("Unknown")
        AddByte("Unknown")
    elif f2 == 5: # Same as 2
        AddInt("Unknown")
        AddInt("Unknown")
        AddByte("Unknown")
    elif f2 == 3: # UI Unknown (154, 155)
        AddInt("Unknown")
        AddInt("Unknown")
        AddByte("Unknown")
    elif f2 == 4: # UI Unknown (150 - TimerDialog, 212)
        AddInt("Unknown")
        AddInt("Unknown")
        AddByte("Unknown")
elif f == 15:
    pass # none
elif f == 16: # GameObjectEffectNifCtx (AddEffectNif)
    AddInt("objectId")
    AddString("nifPath")
    AddBool("isOutline")
    AddFloat("scale")
    AddFloat("rotateZ")
elif f == 17: # (RemoveEffectNif)
    AddInt("objectId") # objectId
elif f == 18: # side pop-up (SideNpcTalk)
    AddByte("type") # 1 = talk, 2  = cutin
    AddInt("duration")
    AddString("UnknownStr")
    AddString("illustration")
    AddString("sound")
    AddString("UnknownStr")
    AddUnicodeString("script")
elif f == 19:
    AddByte("Unknown")
    AddString("UnknownStr")
elif f == 20: # UI: NpcDualHpBarDialog (61, 101)
    b = AddBool("Visible")
    if b:
        AddInt("ObjectId")
        AddInt("durationTick")
        AddInt("npcHpStep")
elif f == 21:
    AddInt("Unknown")
elif f == 22:
    count = AddInt("count")
    for i in range(count):
        AddInt("PlayerObjectId")
    # Additional/Etc/Eff_Target_Select_Keep.xml
    AddUnicodeString("TargetEffect")
elif f == 23:
    count = AddInt("count")
    for i in range(count):
        AddInt("PlayerObjectId")
    # Additional/Etc/Eff_Target_Select_Keep.xml
    AddUnicodeString("TargetEffect")
elif f == 24: # remove above effects?
    pass # none

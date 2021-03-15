from script_api import *

f = AddByte("function")
if f == 1: # start cinematic?
    AddBool("id")
elif f == 2:
    pass # none
elif f == 3:
    AddInt("Unknown")
    AddUnicodeString("UnknownStr")
    AddUnicodeString("UnknownStr")
elif f == 4: # set skip option
    AddByte("type") # 1 = $s_cutscene_skip_scene, 2 = $s_cutscene_skip_state, else: ?
    AddString("skipState")
elif f == 5: # skip cinematic
    pass # none
elif f == 6:
    AddInt("Unknown")
    AddString("Unknown")
    AddUnicodeString("Unknown")
    AddInt("unknown")
    AddByte("unknown")
elif f == 7:
    pass # none
elif f == 8: # add baloon talk
    AddByte("Unknown") # 0 (1=from NPC AI?)
    AddInt("ObjectId") # from spawnPointId
    AddUnicodeString("message")
    AddInt("duration")
    AddInt("delay")
elif f == 9:
    AddInt("Unknown")
elif f == 10: # show caption
    AddUnicodeString("type")
    AddUnicodeString("title")
    AddUnicodeString("desc")
    AddUnicodeString("align")
    AddInt("duration")
    AddFloat("offsetRateX")
    AddFloat("offsetRateY")
    AddFloat("scale")
elif f == 11:
    AddUnicodeString("Unknown")
    AddBool("Unknown")
elif f == 12:
    AddUnicodeString("Unknown")

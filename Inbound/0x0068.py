''' CINEMATIC '''
from script_api import *

f = add_byte("function")
if f == 1: # hide/display ui
    add_bool("hideUi") # true ? 0x620001D : 0x6200041
elif f == 2:
    pass # hideScript, hideDirect (m_bgInstance, m_document)
elif f == 3: # setCinematic
    add_int("type")
    add_unicode_str("scriptString")
    add_unicode_str("UnknownStr") # unused?
elif f == 4: # setSkip
    t = add_byte("type")
    if t == 1:
        pass # 1 = $s_cutscene_skip_scene
    elif t == 2:
        pass # 2 = $s_cutscene_skip_state
    add_str("skipState")
elif f == 5: # start scene skip
    pass # none
elif f == 6: # conversation, UICutSceneCinematic::CinematicTalk
    add_int("npcId")
    add_str("illustrationId")
    add_unicode_str("stringId")
    add_int("delay")
    add_byte("alignFlag") # 0 = top, 1 = center, 2= bottom, 4 = left, 8 = right
elif f == 7: # hideScript
    pass # none
elif f == 8: # add baloon talk
    add_bool("isNpcId") # 0 (1=from NPC AI?)
    add_int("ObjectId") # from spawnPointId
    add_unicode_str("scriptString")
    add_int("duration")
    add_int("delay")
    # UICutSceneCinematic::BalloonGroup, UICutSceneCinematic::BalloonTalk
elif f == 9:
    add_int("ObjectId")
elif f == 10: # show caption
    add_unicode_str("type") # captionType
    add_unicode_str("title") # captionStr1
    add_unicode_str("desc") # captionStr2
    add_unicode_str("align") # captionAlign
    add_int("duration") # captionDuration
    add_float("offsetRateX") # offsetRatioX
    add_float("offsetRateY") # offsetRatioY
    add_float("scale") # captionScale
elif f == 11: # setOpening
    add_unicode_str("scriptString")
    add_bool("Unknown") # passed to setOpening
elif f == 12: # setIntro
    add_unicode_str("scriptString")

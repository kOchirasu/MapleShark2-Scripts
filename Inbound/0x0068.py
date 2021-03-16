from script_api import *

f = add_byte("function")
if f == 1: # start cinematic?
    add_bool("id")
elif f == 2:
    pass # none
elif f == 3:
    add_int("Unknown")
    add_unicode_str("UnknownStr")
    add_unicode_str("UnknownStr")
elif f == 4: # set skip option
    add_byte("type") # 1 = $s_cutscene_skip_scene, 2 = $s_cutscene_skip_state, else: ?
    add_str("skipState")
elif f == 5: # skip cinematic
    pass # none
elif f == 6:
    add_int("Unknown")
    add_str("Unknown")
    add_unicode_str("Unknown")
    add_int("unknown")
    add_byte("unknown")
elif f == 7:
    pass # none
elif f == 8: # add baloon talk
    add_byte("Unknown") # 0 (1=from NPC AI?)
    add_int("ObjectId") # from spawnPointId
    add_unicode_str("message")
    add_int("duration")
    add_int("delay")
elif f == 9:
    add_int("Unknown")
elif f == 10: # show caption
    add_unicode_str("type")
    add_unicode_str("title")
    add_unicode_str("desc")
    add_unicode_str("align")
    add_int("duration")
    add_float("offsetRateX")
    add_float("offsetRateY")
    add_float("scale")
elif f == 11:
    add_unicode_str("Unknown")
    add_bool("Unknown")
elif f == 12:
    add_unicode_str("Unknown")

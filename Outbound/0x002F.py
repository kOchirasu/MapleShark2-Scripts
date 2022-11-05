from script_api import *

f = add_byte("function")
if f == 4:
    pass
elif f == 7:
    pass # used skipped
elif f == 8: # skip cutscene
    add_byte("A")
    add_int("B")
    # SuccessGameProgress: A=12,B=1
    # FailGameProgress: A=12,B=0
    # CGuideActionServerTriggerEvent: A=1,B=?
    # onSwfStop, cut_scene_stop: A=5,B=movieId
elif f == 10: # using computer
    add_int("CubeId") # 130304 when FunctionCubeName=4_130304
elif f == 12: # save script computer
    add_int("CubeId")
    add_str("scriptxml")
elif f == 21:
    add_int("unknown")
    # s_user_trigger_ask_msg_rollback
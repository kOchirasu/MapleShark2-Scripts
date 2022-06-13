''' BUDDY_EMOTE '''
from script_api import *

f = add_byte("Function")
if f == 0:
    add_int("emoteId")
    add_long("characterId")
elif f == 2:
    add_long("senderId")
    message = add_byte("error")
    if message == 1 or message == 2:
        pass # s_couple_emotion_recv_request_in_progressed
    elif message == 3:
        pass
    elif message == 5:
        pass # s_couple_emotion_failed_response_wrong_state_target_user
    elif message == 7:
        pass # s_couple_emotion_target_user_wrong_position
    elif message == 8:
        pass # s_couple_emotion_cannot_request_long_distance
elif f == 3:
    add_int("emoteId")
    add_long("characterId")
    decode_coordF("position")
    decode_coordF("rotation")
    add_float("unknown")
elif f == 4:
    add_int("emoteId")
    add_long("characterId")
elif f == 6:
    add_int("emoteId")
    add_long("characterId")

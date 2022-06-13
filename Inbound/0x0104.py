''' BUDDY_EMOTE '''
from script_api import *

f = add_byte("Function")
if f == 0: # Invite
    add_int("emoteId")
    add_long("characterId") # of requester
    add_unicode_str("name") # of requester
    # Send BuddyEmote (Op 2)
elif f == 1: # Request, s_couple_emotion_request_success
    add_long("characterId")
elif f == 2: # Error
    message = add_byte("message")
    '''
    if message == 0:
        pass # s_couple_emotion_failed_request_not_exist_skill
    elif message == 1:
        pass # s_couple_emotion_failed_request_already_recv
    elif message == 2:
        pass # s_couple_emotion_failed_request_already_in_action
    elif message == 3:
        pass # s_couple_emotion_failed_requset_auto_decline
    elif message == 4:
        pass # s_couple_emotion_failed_accept_request_user_wrong_state
    elif message == 5:
        pass # s_couple_emotion_failed_request_wrong_state_target_user
    elif message == 6:
        pass # s_couple_emotion_failed_accept_cannot_find_request_user
    elif message == 7:
        pass # s_couple_emotion_target_user_wrong_position
    elif message == 8:
        pass # s_couple_emotion_failed_teleport_limit_distance
    elif message == 9:
        pass # s_couple_emotion_cannot_request_in_this_map
    else:
        pass # s_couple_emotion_failed
    '''
elif f == 3: # Accept
    add_int("emoteId")
    add_long("characterId")
elif f == 4: # Decline
    add_int("emoteId")
    add_long("characterId")
elif f == 5: # Start
    add_int("emoteId")
    add_long("characterId 1")
    add_long("characterId 2")
    decode_coordF("position")
    decode_coordF("rotation")
    add_int("unknown")
elif f == 6: # Stop
    add_int("emoteId")
    add_long("characterId")

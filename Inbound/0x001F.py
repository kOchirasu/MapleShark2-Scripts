''' EMOTION '''
from script_api import *

f = add_byte("Function")
if f == 0: # Load Emotion
    count = add_int("Count")
    for i in range(count):
        with Node("Emote " + str(i)):
            add_int("emoteId")
            add_int("Unk (1)")
            add_long("Unk")
elif f == 1: # Learn Emotion
    add_int("emoteId")
    add_int("Unk (1)")
    add_long("Unk")
elif f == 3: # Error
    message = add_byte("message")
    '''
    if message == 0:
        pass # s_dynamic_action_item_invalid
    elif message == 1:
        pass # s_dynamic_action_already_learn
    '''
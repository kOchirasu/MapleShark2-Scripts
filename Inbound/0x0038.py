''' EXP_UP '''
from script_api import *

# Exp up
f = add_byte("Function")
if f == 0:
    # [00] [5A 16 02 00 00 00 00 00] 23 04 5C 3C 1A 00 00 00 00 00 5E 94 89 01 00 00 00 00 00 00 00 00 00
    add_long("NpcGainedExp")
    add_short("level??")
    exp = add_long("PlayerExp")
    add_long("RestExp")
    message = add_int("NpcObjectId or message")
    additional = add_bool("additional")
    '''
    if message == 3000:
        pass # s_msg_take_taxi_exp
    elif message == 3001 or message == 3002:
        pass # s_msg_take_map_exp
    elif message == 3003:
        pass # s_msg_take_telescope_exp
    elif message == 3004 or message == 3007:
        pass # s_msg_take_exp
    elif message == 1059:
        pass # s_msg_take_fishing_exp
    elif message == 1063:
        pass # s_msg_take_play_instrument_exp
    elif message == 1071:
        pass # s_msg_take_arcade_exp
    elif message == 1091:
        pass # s_msg_take_normal_chest_exp
    elif message == 1092:
        pass # s_msg_take_normal_rare_exp
    elif message == 1093:
        pass # s_msg_take_normal_rare_first_exp
    elif message == 60002:
        pass # s_msg_take_assist_bonus_exp, s_msg_take_assist_bonus_exp_system
    else:
        pass # s_msg_take_exp

    if additional:
        pass # s_msg_take_event_additional
    if exp > 0:
        pass # s_msg_take_rest_exp

    # s_msg_take_pcbang some case
    '''
elif f == 1: # set rest exp
    add_long("RestExp")

''' FIELD_ENTRANCE '''
from script_api import *

# dungeon title id
# dungeon goal id
# fame challenge dungeon...?
f = add_byte("Function")
if f == 1:
    pass # s_field_limit_admin
elif f == 2:
    message = add_byte("message")
    add_int("DungeonRoomId")
    # if DungeonRoomId is invalid, s_field_limit_unknown
    '''
    if message == 12:
        pass # s_field_limit_level_min
    elif message == 13:
        pass # s_field_limit_achieve
    elif message == 14:
        pass # s_field_limit_disable_vip
    elif message == 15:
        pass # s_field_limit_gearScore
    elif message == 16:
        pass # s_field_limit_clear_dungeon
    elif message == 17:
        pass # s_field_limit_additionalEffect
    elif message == 18:
        pass # s_dungeon_enter_limit_recommend_weapon
    '''
else:
    count = add_int("count")
    for i in range(count):
        with Node("DungeonRoom " + str(i)):
            add_int("Id")
            add_byte("Unknown") # Eligible?

''' PVP '''
from script_api import *

def decode_pvp_guild_team_result():
    add_unicode_str("unknown")
    add_long("unknown")
    add_int("unknown")
    add_int("unknown")
    add_int("unknown")
    add_unicode_str("unknown")


f = add_byte("function")
if f == 4:
    add_long("unknown")
    add_unicode_str("unknown")
    # s_guild_pvp_done_choose_championship_guild
elif f == 9:
    add_int("unknown")
    # s_individual_register_done
elif f == 10:
    pass # s_individual_unregister_done
elif f == 11:
    add_int("unknown")
    # s_individual_matching_done
    # ... s_msg_popup_time
elif f == 12:
    count = add_byte("count")
    for i in range(count):
        # this could be a long?
        add_int("unknown")
        add_int("unknown")
elif f == 17:
    n = add_int("unknown")
    if n == 0:
        pass # s_rank_duel_ui_error_in_arena_field
elif f == 22: # load
    add_int("Unknown")
    add_int("Score")
    add_int("HighestScore")
    add_int("Unknown")
elif f == 23: # pvp stats
    count = add_int("count")
    for i in range(count):
        with Node("Stats " + str(i), True):
            add_int("JobCode")
            add_int("Wins")
            add_int("Losses")
elif f == 100:
    add_int("objectId")
    with Node("sub_5F1C30", True):
        add_int("MyPC+C")
        add_byte("MyPC+10")
        add_byte("MyPC+20")
elif f == 101:
    add_byte("unknown") # bool?
elif f == 102:
    pass # some delete calls
elif f == 114: # UIPvPGuildTeamDialog
    add_long("unknown")
    add_unicode_str("unknown")
    add_unicode_str("unknown")
    add_long("unknown")
    add_unicode_str("unknown")
    add_unicode_str("unknown")
elif f == 117: # UIPvPGuildTeamResultDialog
    decode_pvp_guild_team_result()
    decode_pvp_guild_team_result()
    n = add_int("unknown")
    '''s_guild_ui_pvp_result_winner_rating / s_guild_ui_pvp_result_loser_rating_add'''
    # s_PvpGuildResult_title_pvp
    if n:
        pass # s_guild_ui_pvp_result_reward

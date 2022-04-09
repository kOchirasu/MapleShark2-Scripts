''' ROOM_DUNGEON '''
from script_api import *

def decode_dungeon_record():
    add_int("DungeonRoomId")
    add_long("ClearDate") # no minutes
    add_byte("Unknown")
    add_byte("Unknown")
    add_long("Unknown")
    add_byte("Unknown")
    add_byte("Unknown")
    add_long("Unknown")
    add_int("Unknown")
    add_short("Unknown")
    add_long("Unknown")
    add_short("Unknown")
    add_byte("Unknown")

def decode_dungeon_rank_reward():
    add_int("DungeonRoomId")
    add_int("Unknown")
    add_long("Unknown")

f = add_byte("Function")
if f == 5:
    count = add_int("Count")
    for i in range(count):
        with Node("DungeonRecord " + str(i)):
            add_int("DungeonRoomId")
            decode_dungeon_record()
elif f == 6: # DungeonRecord
    decode_dungeon_record()
elif f == 7:
    type = add_byte("Type")
    add_int("Argument") # passed as args for type 4
    '''
    if type == 1:
        pass # s_room_dungeon_give_reward
    elif type == 2:
        pass # s_room_dungeon_give_dungeonHelperReward
    elif type == 3:
        pass # s_room_dungeon_reward_addExtraCount
    elif type == 4:
        pass # s_room_dungeon_record_notify_change_expert
    '''
elif f == 9: # UIDungeonExpenseRewardDialog
    add_int("DungeonRoomId")
    add_int("unused?")
elif f == 11: # UIDungeonClosingPhotoDialog
    result = add_byte("result")
    '''
    if result == 1:
        pass # s_room_dungeon_clear
    elif result == 2:
        pass # s_room_dungeon_fail
    '''

    # statistics
    count = add_int("Count")
    for i in range(count):
        add_long("CharacterId")
        type = add_int("type")
        add_int("value")
        '''
        if type == 0:
            pass # s_dungeon_record_accum_damage
        elif type == 1:
            pass # s_dungeon_record_accum_heal
        elif type == 2:
            pass # s_dungeon_record_accum_hit_count
        elif type == 3:
            pass # s_dungeon_record_boss_last_hit
        elif type == 4:
            pass # s_dungeon_record_accum_move_distance
        elif type == 5:
            pass # s_dungeon_record_accum_critical_damage
        elif type == 6:
            pass # s_dungeon_record_max_critial_damage
        elif type == 7:
            pass # s_dungeon_record_accum_monster_kill
        elif type == 8:
            pass # s_dungeon_record_accum_be_hit_count
        elif type == 9:
            pass # s_dungeon_record_accum_default_skill_damage
        '''
elif f == 12: # UIDungeonRewardDialog
    pass # none
elif f == 19: # error
    message = add_int("message")
    add_int("arg")
    if message == 1:
        pass # s_room_party_err_not_chief
    elif message == 2:
        pass # s_room_party_err_full_room
    elif message == 3:
        pass # s_room_dungeon_error_invalidPartyOID
    elif message == 4:
        pass # DungeonRecord
    elif message == 5:
        pass # s_room_dungeon_reward_CantUseExtraReward
    elif message == 6:
        # uses arg
        pass # s_dungeonRoom_lack_extra_ticket
    elif message == 7:
        pass # s_room_dungeon_max_reward_count
    elif message == 8:
        pass # s_room_dungeon_expired
    elif message == 9:
        pass # s_room_dungeon_commingSoon
    elif message == 10:
        pass # s_room_dungeon_canEnterOnDungeonMatch
    elif message == 11:
        pass # s_room_dungeon_canEnterTutorialField
    elif message == 12:
        pass # s_room_dungeon_canEnterDayOfWeeks
    elif message == 13:
        pass # s_room_dungeon_AlreadyChaosHall
    elif message == 14:
        pass # s_room_dungeon_AlreadyLapentaHall
    elif message == 15:
        pass # s_room_dungeon_AlreadyColosseumHall
    elif message == 16:
        pass # s_room_dungeon_CantEnterInDungeon
    elif message == 17:
        pass # s_room_dungeon_OverMaxUserCount
    elif message == 18:
        pass # s_room_dungeon_UnderMinUserCount
    elif message == 19:
        pass # s_room_dungeon_noRewardDayOfWeeks
    elif message == 20:
        pass # s_room_dungeon_HasNotLimitItem
    elif message == 21:
        pass # s_room_dungeon_NotAllowTime
    elif message == 22:
        pass # s_room_dungeon_CantUseAtDungeonRoom
    elif message == 23:
        pass # s_room_dungeon_notOpenTimeDungeon
    elif message == 24:
        pass # s_room_dungeon_cannot_giveup_yet
    elif message == 25:
        pass # s_room_dungeon_require_guild_partry
    elif message == 26:
        pass # s_room_dungeon_require_guild_join_date
    elif message == 27:
        pass # s_room_dungeon_shutdown_find_dungeon_helper
    elif message == 28:
        pass # s_room_dungeon_is_not_open_period_date
    elif message == 29:
        pass # s_room_dungeon_is_not_open_period
    elif message == 30:
        pass # s_room_dungeon_cant_enter_in_partymember
    elif message == 31:
        pass # s_room_dungeon_error_used_reset_united_reward
    elif message == 32:
        pass # s_room_dungeon_error_still_have_united_reawrd
    elif message == 33:
        pass # s_room_dungeon_error_shutdown_united_reawrd_reset
elif f == 20:
    count = add_int("Count")
    for i in range(count):
        with Node("RankReward " + str(i)):
            add_int("DungeonRoomId")
            decode_dungeon_rank_reward()
elif f == 21: # DungeonRankReward
    decode_dungeon_rank_reward()
elif f == 23:
    add_long("Timestamp")
    add_long("CharacterId")

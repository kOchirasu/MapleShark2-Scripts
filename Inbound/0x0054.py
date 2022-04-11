''' PARTY '''
from script_api import *
from common import *

def decode_dungeon_eligibility():
    count = add_int("Count")
    for j in range(count):
        with Node("Entry " + str(j)):
            add_int("Unknown")
            add_byte("Unknown")

def decode_match_party_recruit():
    with Node("PartyListing", True):
        add_long("PartyId")
        add_int("SomeId") # increments somewhat
        add_int("Unknown")
        add_int("Unknown")
        add_unicode_str("PartyName")
        add_bool("IsPublic")
        add_int("MemberCount")
        add_int("MaxMembers")
        add_long("LeaderAccountId")
        add_long("LeaderCharacterId")
        add_unicode_str("LeaderName")
        add_long("CreationTime")

def dungeon_message(message):
    if message == 1:
        pass # s_enum_dungeon_group_normal
    elif message == 2:
        pass # s_enum_dungeon_group_raid
    elif message == 3:
        pass # s_enum_dungeon_group_chaosRaid
    elif message == 4:
        pass # s_enum_dungeon_group_reverseRaid
    elif message == 5:
        pass # s_enum_dungeon_group_lapenta
    elif message == 6:
        pass # s_enum_dungeon_group_guildRaid
    elif message == 7:
        pass # s_enum_dungeon_group_darkStream
    elif message == 8:
        pass # s_enum_dungeon_group_worldBoss
    elif message == 9:
        pass # s_enum_dungeon_group_item
    elif message == 10:
        pass # s_enum_dungeon_group_vip
    elif message == 11:
        pass # s_enum_dungeon_group_event
    elif message == 12:
        pass # s_enum_dungeon_group_fameChallenge
    elif message == 13:
        pass # s_enum_dungeon_group_colosseum
    elif message == 14:
        pass # s_enum_dungeon_group_turka

f = add_byte("function")
if f == 0: # error
    message = add_byte("message")
    add_unicode_str("name")
    '''
    if message == 2:
        pass # s_party_err_full
    elif message == 4:
        pass # s_party_err_not_chief
    elif message == 5:
        pass # s_party_err_already
    elif message == 7 or message == 8 or message == 13:
        pass # s_party_err_not_exist
    elif message == 9:
        pass # s_party_err_deny
    elif message == 10:
        pass # s_party_err_already
    elif message == 11:
        pass # s_party_err_myself
    elif message == 12:
        pass # s_party_err_deny_by_timeout
    elif message == 14:
        pass # s_party_err_cannot_invite
    elif message == 15:
        pass # s_party_err_alreadyInvite
    elif message == 16:
        pass # s_party_err_fail_enterable_result
    elif message == 17:
        pass # s_party_err_lack_level
    elif message == 18:
        pass # s_party_err_lack_gear_score
    elif message == 19:
        pass # s_party_err_full_limit_player
    elif message == 20:
        pass # s_party_err_deny_by_auto
    elif message == 21:
        pass # s_party_err_deny_by_system
    elif message == 22:
        pass # s_party_err_invalid_party
    elif message == 23:
        pass # s_party_err_invalid_chief
    elif message == 24:
        pass # s_party_err_invalid_recruit
    elif message == 25:
        pass # s_party_err_wrong_party
    elif message == 26:
        pass # s_party_err_wrong_recruit
    elif message == 27:
        pass # s_err_lack_merat
    elif message == 28:
        pass # s_party_err_inviteMe
    elif message == 29:
        pass # s_room_party_err_is_in_user
    elif message == 30:
        pass # s_party_invite_boss_room
    elif message == 31:
        pass # s_party_err_not_found
    elif message == 32:
        pass # s_party_request_invite
    elif message == 33:
        pass # s_party_err_already_vote
    elif message == 34:
        pass # s_party_err_vote_need_more_people
    elif message == 35:
        pass # s_party_err_vote_cooldown
    elif message == 36:
        pass # s_party_err_vote_cannot_kick_vote
    elif message == 37:
        pass # s_party_err_vote_cannot_kick_vote_only_dungeon
    elif message == 38:
        pass # s_party_expel_boss_room
    elif message == 39:
        pass # s_party_expel_maple_survival_squad
    elif message == 40:
        pass # s_dungeonMatch_error_isNotChief
    elif message == 41:
        pass # s_dungeonMatch_error_hasOfflineUser
    elif message == 42:
        pass # s_dungeonMatch_error_insideDungeonUser
    elif message == 43:
        pass # s_party_err_dungeon_match_another
    elif message == 44:
        pass # s_party_err_isNotChief
    elif message == 45:
        pass # s_party_err_hasOfflineUser
    elif message == 46:
        pass # s_party_err_inside_survival
    elif message == 47:
        pass # s_party_err_another_matching
    elif message == 48:
        pass # s_party_err_survival_has_solo_register
    elif message == 49:
        pass # s_maple_survival_error_squad_register_over_count
    else:
        pass # s_common_error_unknown
    '''
elif f == 2:
    decode_player()
    decode_dungeon_eligibility()
    # s_party_join_someone
elif f == 3: # left party (Multicast)
    add_long("CharacterId")
    add_bool("self")
    # s_party_leave_someone
elif f == 4: # kicked from party
    add_long("CharacterId")
    # s_party_expel_someone
elif f == 5:
    decode_player()
    # s_party_join_someone
elif f == 6:
    add_long("CharacterId")
    # s_party_member_logout
elif f == 7:
    pass # s_party_break
elif f == 8: # become leader
    add_long("CharacterId")
    # s_party_chief_someone
elif f == 9: # load party
    add_bool("offline")
    add_int("partyId")
    add_long("LeaderUid")
    count = add_byte("count")
    for i in range(count):
        with Node("Member " + str(i)):
            add_bool("Unknown")
            decode_player()
            decode_dungeon_eligibility()
    add_bool("Unknown")
    add_int("DungeonId?")
    add_bool("Unknown")
    b = add_bool("IsPartyListed")
    if b:
        decode_match_party_recruit()
    # s_party_join_me
elif f == 11: # party request
    add_unicode_str("name")
    add_int("partyId")
    # s_msg_party_invite
elif f == 12 or f == 13: # (updating party player)
    add_long("CharacterId")
    decode_player()
elif f == 14:
    add_long("CharacterId")
    decode_dungeon_eligibility()
elif f == 15:
    add_long("Unknown")
    add_int("Unknown")
elif f == 18:
    add_long("Unknown")
    b = add_bool("Unknown")
    if b:
        pass # s_party_member_dead_dark_tomb
    else:
        pass # s_party_member_dead_tomb
elif f == 19: # update stats
    add_long("CharacterId")
    add_long("AccountId")
    add_int("TotalHp")
    add_int("MaxHp")
    add_short("Level?")
elif f == 20: # notice
    add_unicode_str("str_const") # s_party_vote_expired|s_field_enteracne_party_notify_reset_dungeon|s_party_vote_rejected_kick_user
    add_unicode_str("str_const") # Field_Enterance_Reset_Dungeon
    add_unicode_str("Unknown")
elif f == 21:
    b = add_bool("Unknown")
    add_int("Unknown")
    if b:
        add_int("Unknown")
        count = add_int("count")
        for i in range(count):
            add_unicode_str("UnknownStr")
    else:
        add_unicode_str("UnknownStr")
    add_unicode_str("UnknownStr") # effect
elif f == 25: # dungeon reset
    b = add_bool("startedDungeon")
    add_int("DungeonId?")
    if b:
        pass # s_party_create_dungeon, Dungeon_Room_Open
    else:
        pass # s_party_change_help_dungeon
elif f == 26: # party finder
    # true = listed, false = cancel listing
    b = add_bool("IsListed")
    if b:
        decode_match_party_recruit()
elif f == 30: # search party/search party cancel
    type = add_byte("Type") # sub_437040
    '''
    if type == 1:
        dungeon_message(1) # s_enum_dungeon_group_normal
    elif type == 2:
        dungeon_message(8) # s_enum_dungeon_group_worldBoss
    elif type == 3:
        dungeon_message(11) # s_enum_dungeon_group_event
    elif type == 4:
        dungeon_message(5) # s_enum_dungeon_group_lapenta
    else:
        dungeon_message(0)
    '''
    b1 = add_bool("StartSearch") # false = cancel
    b2 = add_bool("Unknown") # must be true
    add_byte("Unknown")
    if b2:
        if b1:
            pass # s_party_match_dungeon_register, Dungeon_Room_searchParty
        else:
            pass # s_party_match_dungeon_unregister, Dungeon_Room_searchPartyCancel
elif f == 31:
    add_long("Unknown")
    # s_party_match_dungeon
elif f == 35: # DungeonRecord related
    add_long("Unknown")
elif f == 37:
    add_long("Unknown")
    add_unicode_str("UnknownStr")
elif f == 40:
    # This value is used as (x / 1000 + 1)
    add_int("Unknown")
    # s_party_find_dungeon_helper_cooldown
elif f == 44: # IGN wants to join your party
    add_unicode_str("name")
    # s_html_chat_invite_party
    # s_html_chat_invite_party_message
    # s_html_chat_system_notice
elif f == 47: # start ready check
    add_bool("Unknown") # vote kick = 1
    with Node("PartyVoteReadyCli"):
        add_int("ReadyCheckConst(34)") # 36 = vote kick
        add_long("timestamp now")
        count = add_int("PartyCount")
        for i in range(count):
            add_long("CharacterId " + str(i))
        count = add_int("ReadyCount")
        for i in range(count):
            add_long("CharacterId " + str(i))
        count = add_int("NotReadyCount")
        for i in range(count):
            add_long("CharacterId " + str(i))
elif f == 48: # not ready
    add_long("CharacterId")
    add_bool("IsReady")
elif f == 49: # ready check expired/completed
    pass # none
elif f == 54: # search party/search party cancel
    b1 = add_bool("StartSearch") # false = cancel
    b2 = add_bool("Unknown") # must be true
    if b2:
        if b1:
            pass # s_maple_survival_squad_register_squad, Dungeon_Room_searchParty
        else:
            pass # s_maple_survival_squad_unregister_squad, Dungeon_Room_searchPartyCancel

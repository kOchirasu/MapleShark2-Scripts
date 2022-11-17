''' GUILD '''
from script_api import *
from common import *
from item import *

def guild_error(message: int):
    if message == 1:
        pass # s_guild_err_unknown
    elif message == 3:
        pass # s_guild_err_null_guild
    elif message == 4:
        pass # s_guild_err_already_exist
    elif message == 5:
        pass # s_guild_err_wait_inviting
    elif message == 6:
        pass # s_guild_err_blocked
    elif message == 7:
        pass # s_guild_err_has_guild
    elif message == 8:
        pass # s_guild_err_invalid_guild
    elif message == 10:
        pass # s_guild_err_null_user
    elif message == 11:
        pass # s_guild_err_name_exist
    elif message == 12:
        pass # s_guild_err_name_value
    elif message == 13:
        pass # s_guild_err_null_member
    elif message == 14:
        pass # s_guild_err_exist_member
    elif message == 15:
        pass # s_guild_err_full_member
    elif message == 16:
        pass # s_guild_err_not_join_member
    elif message == 17:
        pass # s_guild_err_cannot_leave_master
    elif message == 18:
        pass # s_guild_err_expel_target_master
    elif message == 19:
        pass # s_guild_err_not_enough_level
    elif message == 20:
        pass # s_guild_err_no_money
    elif message == 21:
        pass # s_guild_err_no_authority
    elif message == 22:
        pass # s_guild_err_no_master
    elif message == 23:
        pass # s_guild_err_invalid_grade_range
    elif message == 24:
        pass # s_guild_err_invalid_capacity_range
    elif message == 25:
        pass # s_guild_err_invalid_grade_data
    elif message == 26:
        pass # s_guild_err_invalid_grade_index
    elif message == 27:
        pass # s_guild_err_exist_empty_grade_index
    elif message == 28:
        pass # s_guild_err_set_grade_failed
    elif message == 30:
        pass # s_guild_err_fail_addmember
    elif message == 32:
        pass # s_guild_err_null_invite_member
    elif message == 33:
        pass # s_guild_err_cant_during_pvp
    elif message == 34:
        pass # s_guild_extend_capacity_err_cannot
    elif message == 35:
        pass # s_guild_extend_capacity_err_current
    elif message == 36:
        pass # s_guild_search_same_propensity
    elif message == 37:
        pass # s_guild_search_max_join_request
    elif message == 38:
        pass # s_guild_search_last_request
    elif message == 39:
        pass # s_guild_search_null_join_guild_request
    elif message == 41:
        pass # s_guild_err_fail_this_field
    elif message == 42:
        pass # s_guild_err_not_enough_guild_level
    elif message == 43:
        pass # s_guild_err_not_enough_guild_fund
    elif message == 44:
        pass # s_guild_err_cannot_use_skill
    elif message == 45:
        pass # s_guild_err_too_fast_to_search_by_name
    elif message == 46:
        pass # s_guild_pvp_already_pvp_field
    elif message == 47:
        pass # s_guild_err_isNotVsGameTime
    elif message == 48:
        pass # s_guild_err_requireOnlineUserCount
    else:
        pass # s_guild_err_none

def f_59_60_115():
    b1 = add_bool("Result")
    b2 = add_bool("IsRegister")
    if b1:
        if b2:
            pass # s_guild_notify_vsGame_register_ticket
        else:
            pass # s_guild_notify_vsGame_unregister_ticket

def sub_508870():
    add_int("SkillLevel")
    add_int("SkillId (index)")
    add_long("ExpiryTime?")

def decode_pvp_guild_result(): # sub_AE52B0
    add_long("Unknown")
    add_unicode_str("UnknownStr")
    add_unicode_str("UnknownStr")
    add_int("Unknown")
    # s_PvpGuildResult_title_vsGame
    # "win" => s_PvpGuildResult_vsGame_result_win
    # "lose" => s_PvpGuildResult_vsGame_result_lose
    # "draw" => s_PvpGuildResult_vsGame_result_draw

def decode_guild_member():
    with Node("GuildMember"):
        memberType = add_byte("Type (const)") # always 3...
        add_byte("GuildRank")
        add_long("GuildMemberUid")

        if memberType == 3:
            decode_guild_member_player()

            add_unicode_str("GuildMessage")
            add_long("JoinDate")
            add_long("LastLogoffTime")
            add_long("LastLoginTime")
            add_int("Unknown+213")
            add_int("Unknown+217")
            add_int("WeeklyContribution")
            add_int("TotalContribution")
            add_int("DonationCount") # times donated today?
            add_long("LastContributeTime?")
            count2 = add_int("count")
            for j in range(count2):
                add_int("Unknown")
                add_int("Unknown")
            add_bool("IsOffline")
        else:
            add_unicode_str("UnknownStr+114")
            add_int("Unknown+116")
            add_int("Unknown+120")
            add_short("Unknown+124")
            add_unicode_str("UnknownStr+126")

def decode_guild_member_player():
    with Node("PlayerUIEntry"):
        add_long("AccountId")
        add_long("CharacterId")
        add_unicode_str("MemberName")
        add_byte("Gender") # 1
        add_int("JobCode")
        add_int("JobId")
        add_short("Level")
        add_int("GearScore")
        add_int("MapId")
        add_short("Channel ID")
        add_unicode_str("MemberProfileUrl")
        add_int("PlotMapId")
        add_int("PlotId") # 41?
        add_int("ApartmentNumber")
        add_long("PlotExpiration") # By default, but can change...
        for i in range(3):
            add_int("Trophy")

def decode_guild_join_request(): # CGuildJoinRequestForGuild
    with Node("GuildJoinRequest"):
        add_long("ApplicationId")
        add_long("GuildId")
        add_long("ApplicantAccountId")
        add_long("ApplicantCharacterId")
        add_unicode_str("CharacterName")
        add_unicode_str("ProfileUrl")
        add_int("Job")
        add_int("JobCode")
        add_int("Level")
        for i in range(3):
            add_int("Trophy")
        add_long("Timestamp")
    

def decode_guild_join_requestforchar(): # CGuildJoinRequestForChar
    with Node("GuildJoinRequestForChar", True):
        add_long("ApplicationId")
        add_long("GuildId") # 2740883628096919654
        add_unicode_str("GuildName")
        add_int("GuildFocus")
        add_unicode_str("UnknownStr")
        for i in range(3):
            add_int("TotalTrophy")
        add_int("Members")
        add_int("MaxMembers")
        add_unicode_str("UnknownStr")
        add_long("ApplicantAccountId") # 2754957392241780790
        add_long("ApplicantCharacterId") # 2755521558353024091
        add_long("Timestamp")
    

def decode_search_guild_join(): # CSearchGuildJoin
    with Node("SearchGuildJoin", True):
        add_long("GuildUid") # 2740883628096919654
        add_unicode_str("GuildName")
        add_unicode_str("UnknownStr")
        for i in range(3):
            add_int("TotalTrophy")
        add_int("Members")
        add_int("MaxMembers")
        add_int("GuildFocusFlags")
        add_long("LeaderAccountId") # 2757912858338010347
        add_long("LeaderCharacterId") # 2758194333369633524
        add_unicode_str("LeaderName") # Sonic44885
    

def decode_guild_pvp_history_data():
    with Node("GuildPVPHistoryData", True):
        add_int("Unknown")
        add_int("Unknown")
        add_byte("Unknown")
        add_long("Unknown")
        add_long("Unknown")
        add_unicode_str("UnknownStr")
        add_unicode_str("UnknownStr")
        add_int("Unknown")
        add_int("Unknown")
        add_int("Unknown")
        add_int("Unknown")
        for i in range(5):
            with Node("Entry " + str(i)):
                add_unicode_str("UnknownStr")
                add_unicode_str("UnknownStr")
                add_byte("Unknown")
        add_long("Unknown")
        add_long("Unknown")
    

def decode_guild_pvp_season_history_data():
    with Node("GuildPVPSeasonHistoryData"):
        add_int("Unknown")
        add_long("Unknown")
        add_long("Unknown")
        add_unicode_str("UnknownStr")
        add_int("Unknown")
        add_int("Unknown")
        add_int("Unknown")
        add_unicode_str("UnknownStr")
        add_int("Unknown")
        add_int("Unknown")
        add_int("Unknown")
        add_int("Unknown")
        add_int("Unknown")
        add_int("Unknown")
        add_int("Unknown")


# Guild
f = add_byte("Function")
if f == 0:
    add_long("GuildUid")
    add_unicode_str("GuildName")
    add_unicode_str("GuildIconUrl")
    add_byte("MaxMembers")
    add_unicode_str("UnknownStr+22")
    add_unicode_str("GuildMessage")
    add_long("LeaderAccountId")
    add_long("LeaderCharacterId")
    add_unicode_str("GuildLeaderName")
    add_long("CreationTime")
    add_byte("Unknown+52") # 1
    add_int("Unknown+53") # 1000
    add_int("Unknown+57")
    add_int("Unknown+61")
    add_int("Unknown+65")
    add_int("Unknown+69")
    add_int("Unknown+73")
    add_int("Unknown+77")
    add_int("TotalTrophies")
    add_byte("Unknown+85") # 1
    add_int("GuildFocus") # bit-flags
    add_int("GuildExp")
    add_int("GuildFunds")
    add_bool("Unknown+98")
    add_int("Unknown+99")
    with Node("Guild Members"):
        count = add_byte("MemberCount+103")
        for i in range(count):
            decode_guild_member()

    with Node("GuildRanks"):
        count = add_byte("GuildRanksCount")
        for i in range(count):
            decode_guild_rank()
    
    with Node("GuildSkills"):
        count = add_byte("GuildSkillsCount")
        for i in range(count):
            with Node("GuildSkill " + str(i)):
                add_int("SkillId")
                add_int("SkillLevel")
                add_long("ExpireTime")
        
    with Node("GuildEvents"):
        count = add_byte("GuildEventsCount")
        for i in range(count):
            with Node("GuildEvent " + str(i)):
                add_int("Index")
                add_int("Unknown") # 0
    add_int("Guild House Rank")
    add_int("Guild House Theme")
    with Node("GuildPosters"):
        count = add_int("Count")
        for i in range(count):
            with Node("Poster " + str(i)):
                add_int("Index")
                add_unicode_str("PosterUrl")
                add_long("OwnerCharacterId")
                add_unicode_str("OwnerName")

    with Node("GuildNpcs"):
        count = add_byte("Count")
        for i in range(count):
            with Node("GuildNpc " + str(i)):
                add_int("ServiceType")
                add_int("Level")

    with Node("GuildNpcShopProducts"):
        if add_bool("Flag"):
            count = add_short("Count")
            for i in range(count):
                add_bool("Unknown")
                add_short("Unknown")
                add_long("Unknown")
                count2 = add_short("Unknown")
                for j in range(count2):
                    if add_bool("Flag"):
                        add_int("Unknown")
                        add_byte("Unknown")
                        add_int("Unknown")
                        add_int("Unknown")

    with Node("GuildBank"):
        count = add_int("count")
        for i in range(count):
            decode_item_entity()

    add_int("Unknown+149")
    add_unicode_str("UnknownStr+153")
    add_long("Unknown+155")
    add_long("Unknown+163")
    for i in range(7):
        add_int("Unknown")
elif f == 1: # guild created
    e = add_byte("Notice")
    if e == 0:
        add_unicode_str("GuildName")
    else:
        guild_error(e)
elif f == 2: # disband guild
    e = add_byte("Notice") # 0 = success, s_guild_break
    if e != 0:
        guild_error(e)
elif f == 3: # guild invite
    add_unicode_str("Player Name")
elif f == 4:
    decode_guild_invite_info()
elif f == 5: # accepeted to guild
    decode_guild_invite_info()
    b = add_bool("Accepted")
    if b:
        pass # s_guild_join
    else:
        pass # s_guild_join_reject
elif f == 6: # invite response msg
    add_unicode_str("PlayerName")
    add_bool("Accepted")
    e = add_byte("Notice") # 0=accepted, 1=declined, 2, 3
    if e == 0:
        pass # None
    elif e == 1:
        pass # s_guild_join_reject_invite
    elif e == 2:
        pass # s_guild_join_reject_logout
    elif e == 3:
        pass # s_guild_join_reject_timeout
    else:
        pass # s_char_err_name
elif f == 7: # leave guild
    pass # s_guild_leave
elif f == 8: # expell confirm
    add_unicode_str("Name") # name of player expelled
elif f == 9: # expelled from guild
    name = add_unicode_str("Name") # player who expelled you
    if name:
        pass # s_guild_notify_expeled_from
    else:
        pass # s_guild_notify_expeled
elif f == 10: # change player rank
    add_unicode_str("PlayerName")
    add_byte("Rank")
elif f == 11:
    add_unicode_str("UnknownStr")
elif f == 12: # Update member name
    add_unicode_str("OldName")
    add_unicode_str("NewName")
elif f == 14:
    add_unicode_str("PlayerName")
    add_int("Unknown") # 3382??
elif f == 15: # confirm check in
    pass # s_guild_attend_complete
elif f == 18:
    add_unicode_str("AcceptorName") # maybe leader
    add_unicode_str("PlayerName")
    add_byte("Unknown")
    decode_guild_member()
    # s_guild_notify_accept_invite if type == 3
elif f == 19: # leave guild
    add_unicode_str("PlayerName")
    # s_guild_notify_leave
elif f == 20: # kicked player
    add_unicode_str("LeaderName")
    add_unicode_str("PlayerName")
    # s_guild_notify_expel_member
elif f == 21: # updated player rank
    add_unicode_str("LeaderName")
    add_unicode_str("PlayerName")
    add_byte("Rank")
    # s_guild_notify_change_member_grade/s_guild_notify_change_member_grade_me
elif f == 22: # update motto
    add_unicode_str("PlayerName")
    add_unicode_str("PlayerMotto")
elif f == 23: # guild member logged in
    add_unicode_str("PlayerName")
    # s_guild_notify_login_member
elif f == 24: # logged off
    add_unicode_str("PlayerName")
    add_long("LogOFfTime?")
    # s_guild_notify_logout_member
elif f == 25: # become leader
    add_unicode_str("OldLeaderName")
    add_unicode_str("NewLeaderName")
    # s_guild_notify_change_master/s_guild_notify_change_master_me
elif f == 26: # setting notice
    add_unicode_str("LeaderName")
    add_byte("Notice")
    add_unicode_str("NoticeMessage")
    # s_guild_notify_change_notify
elif f == 27: # change emblem
    decode_interface_text()
    add_unicode_str("EmblemUrl")
    # s_guild_notify_change_mark
elif f == 28:
    add_unicode_str("UnknownStr")
    add_int("Unknown")
    # s_guild_notify_change_capacity
elif f == 29: # update rank
    decode_interface_text()
    add_byte("Unknown")
    decode_guild_rank()
    # s_guild_notify_change_grade
elif f == 30: # set guild focus msg (???)
    add_unicode_str("LeaderName")
    # guild focus packet
    add_bool("toggle")
    add_int("FocusFlags")
elif f == 31: # update member location
    add_unicode_str("PlayerName")
    # Some condition, probably if online
    add_int("MapId")
elif f == 32: # update member
    add_unicode_str("PlayerName")
    decode_guild_member_player()
elif f == 33:
    add_unicode_str("PlayerName")
    # s_guild_notify_leave
elif f == 34:
    add_unicode_str("GuildName")
    # s_guild_notify_change_name
elif f == 35: # Achievement
    add_unicode_str("PlayerName")
    add_int("TrophyId")
    add_int("TrophyValue")
    state = add_short("State")
    if state == 2:
        pass # s_guild_notify_achieve_progress
    else:
        pass # s_guild_notify_achieve_complete
elif f == 36: # sent after checking in
    add_unicode_str("Name")
    add_long("TimeNow")
elif f == 37:
    add_unicode_str("UnknownStr")
    add_int("Unknown")
    add_int("Unknown")
elif f == 38: # CUIService Related, addOrUpdateMember
    count = add_int("count")
    for i in range(count):
        add_unicode_str("UnknownStr")
        add_int("Unknown")
        add_int("Unknown")
elif f == 39:
    add_byte("Unknown")
    # s_guild_ui_championship_combat
    # s_guild_ui_championship_my_participate
elif f == 40:
    b = add_bool("Success")
    if b:
        # s_guild_pvp_matching_complete_success
        # s_guild_pvp_matching_complete_popup, s_msg_popup_time
        pass
    else:
        pass # s_guild_pvp_matching_complete_fail
elif f == 41:
    add_int("Unknown") # Guild[63]
    add_int("Unknown") # Guild[64]
    add_int("Unknown") # Guild[65]
    # s_guild_notify_pvp_get_grade
elif f == 42:
    b = add_bool("IsWin")
    add_unicode_str("GuildName")
    if b:
        pass # s_guild_notify_pvp_result_win
    else:
        pass # s_guild_notify_pvp_result_lose
elif f == 43:
    add_unicode_str("GuildName")
    # s_guild_notify_pvp_regist
elif f == 44:
    add_unicode_str("GuildName")
    # s_guild_notify_pvp_unregist
elif f == 45: # receive application
    decode_guild_join_request()
elif f == 46: # application removed
    add_long("ApplicationUid")
elif f == 47: # accept guild invite
    add_unicode_str("AcceptorName")
    add_unicode_str("AcceptedName")
    b = add_bool("Accepted")
    add_long("ApplicationId")
    if b:
        pass # s_guild_notify_search_join_accept
    else:
        pass # s_guild_notify_search_join_reject
elif f == 48: # your application rejected
    add_unicode_str("GuildName")
    add_long("ApplicationId")
    add_byte("Unknown") # 0
elif f == 49: # setGuildExp
    add_int("GuildExp")
elif f == 50: # setGuildFund
    add_int("GuildFunds")
elif f == 51: # update contribution
    add_unicode_str("Name")
    add_int("ContributionGained")
    add_int("WeeklyContribution")
    add_int("TotalContribution")
    # s_guild_gain_contribution
elif f == 52: # Use skill
    add_unicode_str("UsePlayerName")
    sub_508870()
    # s_guild_notify_use_skill_user
elif f == 53: # skill upgraded
    add_unicode_str("UpgraderName")
    sub_508870()
    # s_guild_notify_upgrade_skill
elif f == 54: # started arcade msg
    add_unicode_str("PlayerName") # who started it
    add_int("MinigameId")
    add_int("timestamp (INT)")
    # s_guild_notify_open_event_user
elif f == 55:
    add_unicode_str("PlayerName")
    add_int("HouseRank")
    add_int("HouseTheme")
    # s_guild_notify_house_upgrade
elif f == 56:
    add_long("Unknown")
    add_unicode_str("UnknownStr")
    add_int("Unknown")
    add_unicode_str("UnknownStr")
    # s_guild_notify_change_poster
elif f == 57:
    add_unicode_str("UnknownStr")
    # CGuildNpc related
    add_int("ServiceId")
    add_int("ServiceLevel")
    # s_guild_notify_upgrade_npc
elif f == 59: # RequestMiniGameWar
    f_59_60_115()
    # then calls op 60, 115
elif f == 60:
    f_59_60_115()
    # then calls op 115
elif f == 61: # make leader response
    add_unicode_str("NewLeaderName")
elif f == 62: # set guild notice
    b = add_bool("Success")
    add_unicode_str("GuildNotice")
    if b:
        pass # s_guild_change_notify
elif f == 63: # Change Emblem
    add_unicode_str("EmblemUrl")
elif f == 64:
    add_int("Capacity")
    # s_guild_extend_capacity_success
elif f == 65: # update rank response
    add_byte("RankIndex")
    decode_guild_rank()
    # s_guild_change_grade_sucess
elif f == 66: # set guild focus
    add_bool("toggle")
    add_int("FocusFlags")
elif f == 69: # send mail response
    pass # s_mail_send
elif f == 72: # CGuildPVPHistoryData
    count = add_int("count")
    for i in range(count):
        b = add_bool("flag")
        if b:
            decode_guild_pvp_history_data()
elif f == 73: # CGuildPVPSeasonHistoryData
    count = add_int("count")
    for i in range(count):
        b = add_bool("flag")
        if b:
            decode_guild_pvp_season_history_data()
elif f == 74:
    count = add_int("count")
    for i in range(count):
        add_unicode_str("PlayerName")
        status = add_unicode_str("status")
        add_long("Unknown")
        if status == "expeled":
            pass # s_login_err_main_atl
elif f == 75: # add guild details above player
    add_unicode_str("PlayerName")
    add_unicode_str("GuildName")
elif f == 76: # left/kicked from guild
    add_unicode_str("Name")
elif f == 77: # Error
    add_byte("Unknown") # 1
    message = add_byte("message") # 11
    add_int("Arg") # Used for case 48
    guild_error(message)
elif f == 78:
    add_int("Unknown")
    add_long("Unknown")
    add_long("Unknown")
    add_unicode_str("UnknownStr")
    # s_guild_err_block
elif f == 80: # apply guild
    add_long("ApplicationId")
    add_unicode_str("GuildName")
    # s_guild_search_request_join_guild, sendpacket op 84
elif f == 81: # cancel application
    add_long("ApplicationId")
    add_unicode_str("GuildName")
    # s_guild_search_cancel_request_join_guild, sendpacket op 84
elif f == 82: # response application
    add_long("ApplicationId")
    add_unicode_str("PlayerName")
    b = add_bool("IsAccepted")
    if b:
        pass # s_guild_search_accept_requested_member
    else:
        pass # s_guild_search_reject_requested_member
elif f == 83: # updated players rank?
    count = add_int("count")
    for i in range(count):
        b = add_bool("Requested")
        if b: # CGuildJoinRequestForGuild
             decode_guild_join_request()
elif f == 84: # load open guild search ui (not in guild)
    count = add_int("count")
    for i in range(count):
        b = add_bool("Requested")
        if b: # CGuildJoinRequestForChar
            decode_guild_join_requestforchar()
elif f == 85: # Search for guild
    count = add_int("count")
    for i in range(count):
        b = add_bool("Requested")
        if b: # CSearchGuildJoin
            decode_search_guild_join()
elif f == 88: # active guild buff
    add_int("GuildBuffId")
    # s_guild_skill_use_skill
elif f == 89: # activate guild personal buff
    add_int("GuildBuffId")
elif f == 95: # acquired guild funds/exp
    add_int("AcquiredExp")
    add_int("AcquiredFunds")
    # s_guild_gain_fund
elif f == 96: # start arcade
    add_int("MinigameIndex")
    # s_guild_open_event
elif f == 104:
    add_int("Unknown")
elif f == 106:
    n = add_byte("Unknown")
    if n == 0:
        add_unicode_str("MemberName")
        # s_guild_storage_gift
    elif n == 54:
        pass # s_guild_storage_not_enough_gift_need_period
elif f == 107: # update gift storage
    # Also causes 0x20 to be sent
    decode_item_entity()
elif f == 109: # gift log
    count = add_int("count")
    for i in range(count):
        # Gift Sender
        add_long("AccountId")
        add_long("CharacterId")
        add_unicode_str("Name")
        # Gift Receiver
        add_long("AccountId")
        add_long("CharacterId")
        add_unicode_str("Name")
        decode_item_entity()
        add_long("Timestamp")
elif f == 110: # donate
    add_int("DonationAmount")
    add_long("DonationTime")
    # s_guild_donate_complete
elif f == 114:
    pass # s_guild_notify_vsGame_match_canceled
elif f == 115:
    f_59_60_115()
elif f == 116:
    id = add_int("Unknown")
    if id > 0:
        pass # s_guild_notify_vsGame_open, s_msg_popup_time
elif f == 119:
    decode_pvp_guild_result()
    decode_pvp_guild_result()
elif f == 120:
    t = add_byte("type")
    add_int("Amount")
    if t == 1:
        pass # s_guild_notify_vsGame_reward_exp
    elif t == 2:
        pass # s_guild_notify_vsGame_reward_fund

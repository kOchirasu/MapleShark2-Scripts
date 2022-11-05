''' CLUB '''
from script_api import *

def decode_club():
    add_long("ClubUid")
    add_unicode_str("ClubName")
    add_long("LeaderAccountId")
    add_long("LeaderCharacterId")
    add_unicode_str("LeaderName")
    add_long("CreationTime")
    add_byte("Unknown") # 1
    add_int("Unknown")
    add_int("Unknown")
    add_long("LastNameChangeTimestamp")
    count = add_byte("count")
    for i in range(count):
        decode_club_member()

def decode_club_member():
    with Node("ClubMember"):
        t = add_byte("Type")
        if t == 2:
            add_long("ClubUid")
            decode_club_member_player()
            add_long("JoinTimestamp")
            add_long("LastLogTimestamp")
            add_byte("Online")
        else:
            add_long("Unknown")
            # sub
            add_unicode_str("UnknownStr")
            add_int("Unknown")
            add_int("Unknown")
            add_short("Unknown")
            add_unicode_str("UnknownStr")

def decode_club_member_player():
    with Node("PlayerInfo", True):
        add_long("AccountId")
        add_long("CharacterId")
        add_unicode_str("Name")
        add_byte("Gender")
        add_int("JobCode")
        add_int("JobId")
        add_short("Level")
        add_int("MapId")
        add_short("Unknown") # 0
        add_unicode_str("ProfileUrl")
        add_int("PlotMapId")
        add_int("PlotId") # 41
        add_int("ApartmentNumber")
        add_long("PlotExpiration")
        for i in range(3):
            add_int("Trophy")

def decode_club_packet_invite():
    with Node("ClubPacketInvite"):
        add_long("ClubUid")
        add_unicode_str("ClubName")
        add_unicode_str("ClubLeader")
        add_unicode_str("Invitee")

def club_error(code: int):
    if code == 1:
        pass # s_club_err_unknown
    elif code == 11 or code == 12:
        pass # s_club_err_null_user
    elif code == 13:
        pass # s_club_err_null_member
    elif code == 14:
        pass # s_club_err_null_club
    elif code == 15:
        pass # s_club_err_null_invite_member
    elif code == 51:
        pass # s_club_err_no_master
    elif code == 52:
        pass # s_club_err_not_join_member
    elif code == 53:
        pass # s_club_err_cannot_leave_master
    elif code == 54:
        pass # s_club_err_blocked
    elif code == 55:
        pass # s_club_err_fail_addmember
    elif code == 57:
        pass # s_club_err_full_member
    elif code == 58:
        pass # s_club_err_full_club_member
    elif code == 59:
        pass # 922
    elif code == 60:
        pass # s_club_err_name_exist
    elif code == 61:
        pass # s_club_err_name_value
    elif code == 62:
        pass # s_club_err_exist_member
    elif code == 63:
        pass # s_club_err_already_exist
    elif code == 67:
        pass # s_club_err_notparty_alllogin
    elif code == 72:
        pass # s_club_err_remain_time
    elif code == 73:
        pass # s_club_err_same_club_name
    elif code == 74:
        pass # s_club_err_clubname_has_blank
    else:
        pass # s_club_err_none


f = add_byte("Function")
if f == 0: # load club (after joining)
    decode_club()
elif f == 1: # "The club %s has been created"
    add_long("ClubUid")
    add_unicode_str("ClubName")
elif f == 2: # staged club creation
    decode_club()
    # Send (Club cmd:3), s_club_create_ask, s_msg_popup_time
elif f == 4:
    add_long("ClubUid")
    code = add_byte("ErrorCode") # "ErrorType" = 4
    club_error(code)
elif f == 5: # club could not be created
    add_long("ClubUid")
    add_int("Unknown") # notice code
elif f == 6: # invite player to existing club
    add_long("ClubUid")
    add_unicode_str("PlayerName")
    # s_club_invite_someone
elif f == 7:
    decode_club_packet_invite()
    # s_club_invite_me, s_msg_popup_time
elif f == 8: # accept invite
    decode_club_packet_invite()
    add_int("Unknown")
elif f == 9: # club invite declined
    add_long("ClubUid")
    add_unicode_str("PlayerName")
    add_byte("Unknown") # 0
    add_byte("Unknown") # 1
elif f == 10: # leave club
    add_long("ClubUid")
    # s_club_leave
elif f == 12:
    add_long("ClubUid")
    add_unicode_str("UnknownStr")
elif f == 13: # set club buff (sent to leader only)
    add_long("ClubUid")
    add_int("BuffId")
    add_int("BuffLevel") # 1
elif f == 15: # declined invite(75), club created (0)
    add_long("ClubUid")
    id = add_int("ResponseId") # if == 0, accept. if == 75, reject. if 100 = pending 
    if id == 0:
        pass # s_club_create
    elif id == 76:
        pass # s_club_err_create_reject
    else:
        pass # s_club_err_create
    add_unicode_str("PlayerName")
elif f == 16: # disband club
    add_long("ClubUid")
    add_unicode_str("LeaderName")
    id = add_int("ResponseId")
    if id == 207:
        pass # s_club_break
elif f == 17: # s_club_notify_accept_invite
    add_long("ClubUid")
    add_unicode_str("LeaderName")
    decode_club_member()
elif f == 18: # s_club_notify_leave
    add_long("ClubUid")
    add_unicode_str("PlayerName") 
elif f == 19: # s_club_notify_login_member
    add_long("ClubUid")
    add_unicode_str("UnknownStr")
elif f == 20: # s_club_notify_logout_member
    add_long("ClubUid")
    add_unicode_str("PlayerName")
    add_long("Timestamp")
elif f == 21: # assign new club leader
    add_long("ClubUid")
    add_unicode_str("PreviousLeaderName")
    add_unicode_str("NewLeaderName")
    b = add_bool("Unknown")
    # s_club_notify_change_master/s_club_notify_change_master_me
elif f == 22: # s_club_notify_change_buff (BROADCAST)
    add_long("ClubUid")
    add_int("BuffId")
    add_int("Unknown") # 1
elif f == 23: # update member location
    add_long("ClubUid")
    add_unicode_str("PlayerName")
    add_int("MapId")
elif f == 24: # update club member
    add_long("ClubUid")
    add_unicode_str("MemberName")
    decode_club_member_player()
elif f == 25: # s_club_notify_leave??
    add_long("ClubUid")
    add_unicode_str("PlayerName")
elif f == 26: # s_club_notify_change_name
    add_long("ClubUid")
    add_unicode_str("ClubName")
    add_long("Timestamp")
elif f == 27: # update club member's name
    add_long("CharacterId")
    add_unicode_str("PreviousName")
    add_unicode_str("NewName")
elif f == 28:
    add_long("ClubUid")
    add_unicode_str("UnknownStr")
elif f == 29: # Error
    add_byte("ErrorType?")
    code = add_int("ErrorCode")
    club_error(code)
elif f == 30: # left club, joined club
    add_long("ClubUid")
    add_unicode_str("PlayerName")
    add_unicode_str("ClubName") # Empty when leaving

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
    add_long("Unknown")
    count = add_byte("count")
    for i in range(count):
        decode_club_member()

def decode_club_member():
    with Node("ClubMember"):
        t = add_byte("Type")
        if t == 2:
            add_long("Unknown")
            decode_club_member_player()
            add_long("Unknown")
            add_long("Unknown")
            add_byte("Unknown")
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
        add_int("Unknown")
        add_long("PlotExpiration")
        for i in range(3):
            add_int("Trophy")

def decode_club_packet_invite():
    with Node("ClubPacketInvite"):
        add_long("ClubUid")
        add_unicode_str("ClubName")
        add_unicode_str("ClubLeader")
        add_unicode_str("Invitee")


f = add_byte("Function")
if f == 0: # load club (after joining)
    decode_club()
elif f == 1: # "The club %s has been created"
    add_long("ClubUid")
    add_unicode_str("ClubName")
elif f == 2: # staged club creation
    decode_club()
elif f == 4:
    add_long("Unknown")
    add_byte("Unknown")
elif f == 5: # club could not be created
    add_long("ClubUid")
    add_int("Unknown") # notice code
elif f == 6: # invite player to existing club
    add_long("ClubUid")
    add_unicode_str("PlayerName")
elif f == 7:
    decode_club_packet_invite()
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
elif f == 12:
    add_long("ClubUid")
    add_unicode_str("UnknownStr")
elif f == 13: # set club buff (sent to leader only)
    add_long("ClubUid")
    add_int("BuffId")
    add_int("Unknown") # 1
elif f == 15: # declined invite(75), club created (0)
    add_long("ClubUid")
    add_int("Unknown") # 75?
    add_unicode_str("PlayerName")
elif f == 16:
    add_long("ClubUid")
    add_unicode_str("UnknownStr")
    add_int("Unknown") # if == 207 display some notice
elif f == 17: # %s has accepted %s's invite to the club
    add_long("ClubUid")
    add_unicode_str("LeaderName?")
    decode_club_member()
elif f == 18:
    add_long("ClubUid")
    add_unicode_str("UnknownStr")
elif f == 19:
    add_long("ClubUid")
    add_unicode_str("UnknownStr")
elif f == 20: # club member log off
    add_long("ClubUid")
    add_unicode_str("PlayerName")
    add_long("Timestamp")
elif f == 21:
    add_long("ClubUid")
    add_unicode_str("UnknownStr")
    add_unicode_str("UnknownStr")
    add_byte("Unknown")
elif f == 22: # set club buff (sent to all)
    add_long("ClubUid")
    add_int("BuffId")
    add_int("Unknown") # 1
elif f == 23:
    add_long("ClubUid")
    add_unicode_str("UnknownStr")
elif f == 24: # update club member
    add_long("ClubUid")
    add_unicode_str("MemberName")
    decode_club_member_player()
elif f == 25:
    add_long("ClubUid")
    add_unicode_str("UnknownStr")
elif f == 26: # change name
    add_long("ClubUid")
    add_unicode_str("ClubName")
    add_long("Timestamp")
elif f == 27:
    add_long("Unknown")
    add_unicode_str("UnknownStr")
    add_unicode_str("UnknownStr")
elif f == 28:
    add_long("ClubUid")
    add_unicode_str("UnknownStr")
elif f == 29: # Error
    add_byte("ErrorType?")
    add_int("ErrorCode")
elif f == 30: # left club, joined club
    add_long("ClubUid")
    add_unicode_str("PlayerName")
    add_unicode_str("ClubName") # Empty when leaving

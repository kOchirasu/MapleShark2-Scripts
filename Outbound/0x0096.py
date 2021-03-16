from script_api import *

def decode_club_packet_invite():
    with Node("ClubPacketInvite"):
        add_long("ClubUid")
        add_unicode_str("ClubName")
        add_unicode_str("ClubLeader")
        add_unicode_str("Invitee")
    

f = add_byte("Function")
if f == 1: # create club name (from party)
    add_unicode_str("ClubName")
elif f == 3: # respond club from party
    add_long("ClubUid")
    add_int("Unknown") # 0 = create, 75 = decline
elif f == 6: # invite player to existing club
    add_long("ClubUid")
    add_unicode_str("PlayerName")
elif f == 8: # accept invite
    decode_club_packet_invite()
    add_bool("Accepted") # 1 = accept, 0 = decline
elif f == 10: # leave club
    add_long("ClubUid")
elif f == 12:
    add_byte("Unknown")
    add_long("Unknown")
    add_unicode_str("UnknownStr")
elif f == 13:
    add_long("ClubUid")
    add_int("BuffId")
    add_int("Unknown") # 1
elif f == 14: # change name
    add_long("ClubUid")
    add_unicode_str("NewName")

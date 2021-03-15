from script_api import *

def DecodeClubPacketInvite():
    with Node("ClubPacketInvite"):
        AddLong("ClubUid")
        AddUnicodeString("ClubName")
        AddUnicodeString("ClubLeader")
        AddUnicodeString("Invitee")
    

f = AddByte("Function")
if f == 1: # create club name (from party)
    AddUnicodeString("ClubName")
elif f == 3: # respond club from party
    AddLong("ClubUid")
    AddInt("Unknown") # 0 = create, 75 = decline
elif f == 6: # invite player to existing club
    AddLong("ClubUid")
    AddUnicodeString("PlayerName")
elif f == 8: # accept invite
    DecodeClubPacketInvite()
    AddBool("Accepted") # 1 = accept, 0 = decline
elif f == 10: # leave club
    AddLong("ClubUid")
elif f == 12:
    AddByte("Unknown")
    AddLong("Unknown")
    AddUnicodeString("UnknownStr")
elif f == 13:
    AddLong("ClubUid")
    AddInt("BuffId")
    AddInt("Unknown") # 1
elif f == 14: # change name
    AddLong("ClubUid")
    AddUnicodeString("NewName")

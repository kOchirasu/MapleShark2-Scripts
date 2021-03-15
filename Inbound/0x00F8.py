from script_api import *

def DecodeClub():
    AddLong("ClubUid")
    AddUnicodeString("ClubName")
    AddLong("LeaderAccountId")
    AddLong("LeaderCharacterId")
    AddUnicodeString("LeaderName")
    AddLong("CreationTime")
    AddByte("Unknown") # 1
    AddInt("Unknown")
    AddInt("Unknown")
    AddLong("Unknown")
    count = AddByte("count")
    for i in range(count):
        DecodeClubMember()

def DecodeClubMember():
    with Node("ClubMember"):
        t = AddByte("Type")
        if t == 2:
            AddLong("Unknown")
            DecodeClubMemberPlayer()
            AddLong("Unknown")
            AddLong("Unknown")
            AddByte("Unknown")
        else:
            AddLong("Unknown")
            # sub
            AddUnicodeString("UnknownStr")
            AddInt("Unknown")
            AddInt("Unknown")
            AddShort("Unknown")
            AddUnicodeString("UnknownStr")

def DecodeClubMemberPlayer():
    with Node("PlayerInfo", True):
        AddLong("AccountId")
        AddLong("CharacterId")
        AddUnicodeString("Name")
        AddByte("Gender")
        AddInt("JobCode")
        AddInt("JobId")
        AddShort("Level")
        AddInt("MapId")
        AddShort("Unknown") # 0
        AddUnicodeString("ProfileUrl")
        AddInt("PlotMapId")
        AddInt("PlotId") # 41
        AddInt("Unknown")
        AddLong("PlotExpiration")
        for i in range(3):
            AddInt("Trophy")

def DecodeClubPacketInvite():
    with Node("ClubPacketInvite"):
        AddLong("ClubUid")
        AddUnicodeString("ClubName")
        AddUnicodeString("ClubLeader")
        AddUnicodeString("Invitee")


f = AddByte("Function")
if f == 0: # load club (after joining)
    DecodeClub()
elif f == 1: # "The club %s has been created"
    AddLong("ClubUid")
    AddUnicodeString("ClubName")
elif f == 2: # staged club creation
    DecodeClub()
elif f == 4:
    AddLong("Unknown")
    AddByte("Unknown")
elif f == 5: # club could not be created
    AddLong("ClubUid")
    AddInt("Unknown") # notice code
elif f == 6: # invite player to existing club
    AddLong("ClubUid")
    AddUnicodeString("PlayerName")
elif f == 7:
    DecodeClubPacketInvite()
elif f == 8: # accept invite
    DecodeClubPacketInvite()
    AddInt("Unknown")
elif f == 9: # club invite declined
    AddLong("ClubUid")
    AddUnicodeString("PlayerName")
    AddByte("Unknown") # 0
    AddByte("Unknown") # 1
elif f == 10: # leave club
    AddLong("ClubUid")
elif f == 12:
    AddLong("ClubUid")
    AddUnicodeString("UnknownStr")
elif f == 13: # set club buff (sent to leader only)
    AddLong("ClubUid")
    AddInt("BuffId")
    AddInt("Unknown") # 1
elif f == 15: # declined invite(75), club created (0)
    AddLong("ClubUid")
    AddInt("Unknown") # 75?
    AddUnicodeString("PlayerName")
elif f == 16:
    AddLong("ClubUid")
    AddUnicodeString("UnknownStr")
    AddInt("Unknown") # if == 207 display some notice
elif f == 17: # %s has accepted %s's invite to the club
    AddLong("ClubUid")
    AddUnicodeString("LeaderName?")
    DecodeClubMember()
elif f == 18:
    AddLong("ClubUid")
    AddUnicodeString("UnknownStr")
elif f == 19:
    AddLong("ClubUid")
    AddUnicodeString("UnknownStr")
elif f == 20: # club member log off
    AddLong("ClubUid")
    AddUnicodeString("PlayerName")
    AddLong("Timestamp")
elif f == 21:
    AddLong("ClubUid")
    AddUnicodeString("UnknownStr")
    AddUnicodeString("UnknownStr")
    AddByte("Unknown")
elif f == 22: # set club buff (sent to all)
    AddLong("ClubUid")
    AddInt("BuffId")
    AddInt("Unknown") # 1
elif f == 23:
    AddLong("ClubUid")
    AddUnicodeString("UnknownStr")
elif f == 24: # update club member
    AddLong("ClubUid")
    AddUnicodeString("MemberName")
    DecodeClubMemberPlayer()
elif f == 25:
    AddLong("ClubUid")
    AddUnicodeString("UnknownStr")
elif f == 26: # change name
    AddLong("ClubUid")
    AddUnicodeString("ClubName")
    AddLong("Timestamp")
elif f == 27:
    AddLong("Unknown")
    AddUnicodeString("UnknownStr")
    AddUnicodeString("UnknownStr")
elif f == 28:
    AddLong("ClubUid")
    AddUnicodeString("UnknownStr")
elif f == 29: # Error
    AddByte("ErrorType?")
    AddInt("ErrorCode")
elif f == 30: # left club, joined club
    AddLong("ClubUid")
    AddUnicodeString("PlayerName")
    AddUnicodeString("ClubName") # Empty when leaving

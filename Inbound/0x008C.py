from script_api import *
from common import *

def f_59_60_115():
    AddBool("Unknown")
    AddBool("Unknown")

def sub_508870():
    AddInt("SkillLevel")
    AddInt("SkillId (index)")
    AddLong("ExpiryTime?")

def sub_AE52B0():
    AddLong("Unknown")
    AddUnicodeString("UnknownStr")
    AddUnicodeString("UnknownStr")
    AddInt("Unknown")

def DecodeGuildMember():
    with Node("GuildMember"):
        memberType = AddByte("Type (const)") # always 3...
        AddByte("GuildRank")
        AddLong("GuildMemberUid")

        if memberType == 3:
            DecodeGuildMemberPlayer()

            AddUnicodeString("GuildMessage")
            AddLong("JoinDate")
            AddLong("LastLogoffTime")
            AddLong("LastLoginTime")
            AddInt("Unknown+213")
            AddInt("Unknown+217")
            AddInt("WeeklyContribution")
            AddInt("TotalContribution")
            AddInt("DonationCount") # times donated today?
            AddLong("LastContributeTime?")
            count2 = AddInt("count")
            for j in range(count2):
                AddInt("Unknown")
                AddInt("Unknown")
            AddBool("CanCheckIn?")
        else:
            AddUnicodeString("UnknownStr+114")
            AddInt("Unknown+116")
            AddInt("Unknown+120")
            AddShort("Unknown+124")
            AddUnicodeString("UnknownStr+126")

def DecodeGuildMemberPlayer():
    with Node("PlayerUIEntry"):
        AddLong("AccountId")
        AddLong("CharacterId")
        AddUnicodeString("MemberName")
        AddByte("Gender") # 1
        AddInt("JobCode")
        AddInt("JobId")
        AddShort("Level")
        AddInt("GearScore")
        AddInt("MapId")
        AddShort("Unknown+151") # 0
        AddUnicodeString("MemberProfileUrl")
        AddInt("PlotMapId")
        AddInt("PlotId") # 41?
        AddInt("Unknown+163")
        AddLong("PlotExpiration") # By default, but can change...
        for i in range(3):
            AddInt("Trophy")

def DecodeGuildJoinRequest(): # CGuildJoinRequestForGuild
    with Node("GuildJoinRequest"):
        AddLong("Unknown")
        AddLong("Unknown")
        AddLong("Unknown")
        AddLong("Unknown")
        AddUnicodeString("UnknownStr")
        AddUnicodeString("UnknownStr")
        AddInt("Unknown")
        AddInt("Unknown")
        AddInt("Unknown")
        AddLong("Unknown")
    

def DecodeGuildJoinRequestForChar(): # CGuildJoinRequestForChar
    with Node("GuildJoinRequestForChar", True):
        AddLong("ApplicationId")
        AddLong("GuildId") # 2740883628096919654
        AddUnicodeString("GuildName")
        AddInt("GuildFocus")
        AddUnicodeString("UnknownStr")
        for i in range(3):
            AddInt("TotalTrophy")
        AddInt("Members")
        AddInt("MaxMembers")
        AddUnicodeString("UnknownStr")
        AddLong("ApplicantAccountId") # 2754957392241780790
        AddLong("ApplicantCharacterId") # 2755521558353024091
        AddLong("Timestamp")
    

def DecodeSearchGuildJoin(): # CSearchGuildJoin
    with Node("SearchGuildJoin", True):
        AddLong("GuildUid") # 2740883628096919654
        AddUnicodeString("GuildName")
        AddUnicodeString("UnknownStr")
        for i in range(3):
            AddInt("TotalTrophy")
        AddInt("Members")
        AddInt("MaxMembers")
        AddInt("GuildFocusFlags")
        AddLong("LeaderAccountId") # 2757912858338010347
        AddLong("LeaderCharacterId") # 2758194333369633524
        AddUnicodeString("LeaderName") # Sonic44885
    

def DecodeGuildPVPHistoryData():
    with Node("GuildPVPHistoryData", True):
        AddInt("Unknown")
        AddInt("Unknown")
        AddByte("Unknown")
        AddLong("Unknown")
        AddLong("Unknown")
        AddUnicodeString("UnknownStr")
        AddUnicodeString("UnknownStr")
        AddInt("Unknown")
        AddInt("Unknown")
        AddInt("Unknown")
        AddInt("Unknown")
        for i in range(5):
            with Node("Entry " + str(i)):
                AddUnicodeString("UnknownStr")
                AddUnicodeString("UnknownStr")
                AddByte("Unknown")
        AddLong("Unknown")
        AddLong("Unknown")
    

def DecodeGuildPVPSeasonHistoryData():
    with Node("GuildPVPSeasonHistoryData"):
        AddInt("Unknown")
        AddLong("Unknown")
        AddLong("Unknown")
        AddUnicodeString("UnknownStr")
        AddInt("Unknown")
        AddInt("Unknown")
        AddInt("Unknown")
        AddUnicodeString("UnknownStr")
        AddInt("Unknown")
        AddInt("Unknown")
        AddInt("Unknown")
        AddInt("Unknown")
        AddInt("Unknown")
        AddInt("Unknown")
        AddInt("Unknown")
    

def DecodeGuildBankEntry():
    with Node("UnknownEntry"):
        AddInt("ItemId")
        AddShort("Rarity")
        AddInt("Amount")
        AddBool("Unknown")
        AddBool("Unknown")
        AddBool("Unknown")
        AddBool("Unknown")


# Guild
f = AddByte("Function")
if f == 0:
    AddLong("GuildUid")
    AddUnicodeString("GuildName")
    AddUnicodeString("GuildIconUrl")
    AddByte("MaxMembers")
    AddUnicodeString("UnknownStr+22")
    AddUnicodeString("GuildMessage")
    AddLong("LeaderAccountId")
    AddLong("LeaderCharacterId")
    AddUnicodeString("GuildLeaderName")
    AddLong("CreationTime")
    AddByte("Unknown+52")
    AddInt("Unknown+53") # 1000
    AddInt("Unknown+57")
    AddInt("Unknown+61")
    AddInt("Unknown+65")
    AddInt("Unknown+69")
    AddInt("Unknown+73")
    AddInt("Unknown+77")
    AddInt("Unknown+81")
    AddByte("Unknown+85") # 1
    AddInt("GuildFocus") # bit-flags
    AddInt("GuildExp")
    AddInt("GuildFunds")
    AddBool("Unknown+98")
    AddInt("Unknown+99")
    with Node("Guild Members"):
        count = AddByte("MemberCount+103")
        for i in range(count):
            DecodeGuildMember()

    with Node("GuildRanks"):
        count = AddByte("GuildRanksCount")
        for i in range(count):
            DecodeGuildRank()
    
    with Node("GuildSkills"):
        count = AddByte("GuildSkillsCount")
        for i in range(count):
            with Node("GuildSkill " + str(i)):
                AddInt("SkillId")
                AddInt("SkillLevel")
                AddLong("ExpireTime")
        
    with Node("GuildEvents"):
        count = AddByte("GuildEventsCount")
        for i in range(count):
            with Node("GuildEvent " + str(i)):
                AddInt("Index")
                AddInt("Unknown") # 0
        
    with Node("GuildPosters"):
        AddInt("Unknown+131")
        AddInt("Unknown+135")
        count = AddInt("Count")
        for i in range(count):
            with Node("Poster " + str(i)):
                AddInt("Index")
                AddUnicodeString("PosterUrl")
                AddLong("OwnerCharacterId")
                AddUnicodeString("OwnerName")
            
    with Node("GuildNpcs"):
        count = AddByte("Count")
        for i in range(count):
            with Node("GuildNpc " + str(i)):
                AddInt("ServiceType")
                AddInt("Level")
        
    with Node("GuildNpcShopProducts"):
        if AddBool("Flag"):
            count = AddShort("Count")
            for i in range(count):
                AddBool("Unknown")
                AddShort("Unknown")
                AddLong("Unknown")
                count2 = AddShort("Unknown")
                for j in range(count2):
                    if AddBool("Flag"):
                        AddInt("Unknown")
                        AddByte("Unknown")
                        AddInt("Unknown")
                        AddInt("Unknown")
    
    with Node("GuildBank"):
        count = AddInt("count")
        for i in range(count):
            DecodeGuildBankEntry()
    
    AddInt("Unknown+149")
    AddUnicodeString("UnknownStr+153")
    AddLong("Unknown+155")
    AddLong("Unknown+163")
    for i in range(7):
        AddInt("Unknown")
elif f == 1: # guild created
    e = AddByte("Notice")
    if e == 0:
        AddUnicodeString("GuildName")
elif f == 2: # disband guild
    e = AddByte("Notice") # 0 = success
elif f == 3: # guild invite
    AddUnicodeString("Player Name")
elif f == 4:
    DecodeGuildInviteInfo()
elif f == 5: # accepeted to guild
    DecodeGuildInviteInfo()
    AddBool("Notice")
elif f == 6: # invite response msg
    AddUnicodeString("PlayerName")
    b = AddByte("Unknown") # T if accept
    AddByte("Notice") # 0=accepted, 1=declined, 2, 3
    if b != 1:
        pass # Display Notice
elif f == 7: # leave guild
    pass # notice
elif f == 8:
    AddUnicodeString("UnknownStr")
elif f == 9:
    AddUnicodeString("UnknownStr")
elif f == 10: # change player rank
    AddUnicodeString("PlayerName")
    AddByte("Rank")
elif f == 11:
    AddUnicodeString("UnknownStr")
elif f == 12:
    AddUnicodeString("UnknownStr")
    AddUnicodeString("UnknownStr")
elif f == 14:
    AddUnicodeString("PlayerName")
    AddInt("Unknown") # 3382??
elif f == 15: # confirm check in
    pass # none
elif f == 18:
    AddUnicodeString("AcceptorName") # maybe leader
    AddUnicodeString("PlayerName")
    AddByte("Unknown")
    DecodeGuildMember()
elif f == 19:
    AddUnicodeString("UnknownStr")
elif f == 20: # kicked player
    AddUnicodeString("LeaderName")
    AddUnicodeString("PlayerName")
elif f == 21: # updated player rank
    AddUnicodeString("LeaderName")
    AddUnicodeString("PlayerName")
    AddByte("Rank")
elif f == 22: # update motto
    AddUnicodeString("PlayerName")
    AddUnicodeString("PlayerMotto")
elif f == 23: # guild member logged in
    AddUnicodeString("PlayerName")
elif f == 24: # logged off
    AddUnicodeString("PlayerName")
    AddLong("LogOFfTime?")
elif f == 25: # become leader
    AddUnicodeString("OldLeaderName")
    AddUnicodeString("NewLeaderName")
elif f == 26: # setting notice
    AddUnicodeString("LeaderName")
    AddByte("Notice")
    AddUnicodeString("NoticeMessage")
elif f == 27:
    AddUnicodeString("UnknownStr")
elif f == 28:
    AddUnicodeString("UnknownStr")
    AddInt("Unknown")
elif f == 29: # update rank
    b = AddBool("Unknown")
    AddInt("Unknown")
    if not b:
        AddUnicodeString("LeaderName")
    else:
        AddInt("Unknown")
        count = AddInt("count")
        for i in range(count):
            AddUnicodeString("UnknownStr")
    AddByte("Unknown")
    DecodeGuildRank()
elif f == 30: # set guild focus msg (???)
    AddUnicodeString("LEaderName")
    # guild focus packet
    AddBool("Unkown")
    AddInt("FocusFlags")
elif f == 31:
    AddUnicodeString("UnknownStr")
    # Some condition
    # AddInt("Unknown")
elif f == 32: # update member
    AddUnicodeString("PlayerName")
    DecodeGuildMemberPlayer()
elif f == 33:
    AddUnicodeString("UnknownStr")
elif f == 34:
    AddUnicodeString("UnknownStr")
elif f == 35:
    AddUnicodeString("UnknownStr")
    AddInt("Unknown")
    AddInt("Unknown")
    AddShort("Unknown")
elif f == 36: # sent after updating contribution?
    AddUnicodeString("Name")
    AddLong("TimeNow")
elif f == 37:
    AddUnicodeString("UnknownStr")
    AddInt("Unknown")
    AddInt("Unknown")
elif f == 38: # CUIService Related
    count = AddInt("count")
    for i in range(count):
        AddUnicodeString("UnknownStr")
        AddInt("Unknown")
        AddInt("Unknown")
elif f == 39:
    AddByte("Unknown")
elif f == 40:
    AddByte("Unknown")
elif f == 41:
    AddInt("Unknown")
    AddInt("Unknown")
    AddInt("Unknown")
elif f == 42:
    AddByte("Unknown")
    AddUnicodeString("UnknownStr")
elif f == 43:
    AddUnicodeString("UnknownStr")
elif f == 44:
    AddUnicodeString("UnknownStr")
elif f == 45: # receive application
    DecodeGuildJoinRequest()
elif f == 46: # application removed
    AddLong("ApplicationUid")
elif f == 47: # accept guild invite
    AddUnicodeString("AcceptorName")
    AddUnicodeString("AcceptedName")
    AddByte("1 when accepted")
    AddLong("ApplicationId")
elif f == 48: # your application rejected
    AddUnicodeString("GuildName")
    AddLong("ApplicationId")
    AddByte("Unknown") # 0
elif f == 49: # update guild exp
    AddInt("GuildExp") # 3307547 (GuildExp?)
elif f == 50: # update guild funds
    AddInt("GuildFunds")
elif f == 51: # update contribution
    AddUnicodeString("Name")
    AddInt("ContributionGained")
    AddInt("WeeklyContribution")
    AddInt("TotalContribution")
elif f == 52: # Use skill
    AddUnicodeString("UsePlayerName")
    sub_508870()
elif f == 53: # skill upgraded
    AddUnicodeString("UpgraderName")
    sub_508870()
elif f == 54: # started arcade msg
    AddUnicodeString("PlayerName") # who started it
    AddInt("GameIndex")
    AddInt("timestamp (INT)")
elif f == 55:
    AddUnicodeString("UnknownStr")
    AddInt("Unknown")
    AddInt("Unknown")
elif f == 56:
    AddLong("Unknown")
    AddUnicodeString("UnknownStr")
    AddInt("Unknown")
    AddUnicodeString("UnknownStr")
elif f == 57:
    AddUnicodeString("UnknownStr")
    # CGuildNpc related
    AddInt("Unknown")
    AddInt("Unknown")
elif f == 59:
    f_59_60_115()
elif f == 60:
    f_59_60_115()
elif f == 61: # make leader response
    AddUnicodeString("NewLeaderName")
elif f == 62: # set guild notice
    AddBool("Unknown") # 1
    AddUnicodeString("GuildNotice")
elif f == 63:
    AddUnicodeString("UnknownStr")
elif f == 64:
    AddInt("Unknown")
elif f == 65: # update rank response
    AddByte("Unknown")
    DecodeGuildRank()
elif f == 66: # set guild focus
    AddBool("Unkown")
    AddInt("FocusFlags")
elif f == 69: # send mail response
    pass # none
elif f == 72:
    count = AddInt("count")
    for i in range(count):
        b = AddBool("flag")
        if b:
            DecodeGuildPVPHistoryData()
elif f == 73:
    count = AddInt("count")
    for i in range(count):
        b = AddBool("flag")
        if b:
            DecodeGuildPVPSeasonHistoryData()
elif f == 74:
    count = AddInt("count")
    for i in range(count):
        AddUnicodeString("UnknownStr")
        AddUnicodeString("UnknownStr")
        AddLong("Unknown")
elif f == 75: # add guild details above player
    AddUnicodeString("PlayerName")
    AddUnicodeString("GuildName")
elif f == 76: # left/kicked from guild
    AddUnicodeString("Name")
elif f == 77: # create guild name taken
    AddByte("Unknown") # 1
    AddByte("Unknown") # 11
    AddInt("Unknown")
elif f == 78:
    AddInt("Unknown")
    AddLong("Unknown")
    AddLong("Unknown")
    AddUnicodeString("UnknownStr")
elif f == 80: # apply guild
    AddLong("ApplicationId")
    AddUnicodeString("GuildName")
elif f == 81: # cancel application
    AddLong("ApplicationId")
    AddUnicodeString("GuildName")
elif f == 82: # response application
    AddLong("ApplicationId")
    AddUnicodeString("PlayerName")
    AddBool("IsAccepted") # 0
elif f == 83: # updated players rank?
    count = AddInt("count")
    for i in range(count):
        b = AddBool("Unknown")
        if b:
             DecodeGuildJoinRequest()
elif f == 84: # load open guild search ui (not in guild)
    count = AddInt("count")
    for i in range(count):
        b = AddBool("Requested")
        if b:
            DecodeGuildJoinRequestForChar()
elif f == 85: # Search for guild
    count = AddInt("count")
    for i in range(count):
        b = AddBool("Unknown")
        if b:
            DecodeSearchGuildJoin()
elif f == 88: # active guild buff
    AddInt("GuildBuffId")
elif f == 89: # activate guild personal buff
    AddInt("GuildBuffId")
elif f == 95: # acquired guild funds/exp (msg)
    AddInt("AcquiredExp")
    AddInt("AcquiredFunds")
elif f == 96: # start arcade
    AddInt("MinigameIndex")
elif f == 104:
    AddInt("Unknown")
elif f == 106:
    b = AddBool("Unknown")
    if not b:
        AddUnicodeString("UnknownStr")
elif f == 107: # update gift storage
    # Also causes 0x20 to be sent
    DecodeGuildBankEntry()
elif f == 109: # gift log
    count = AddInt("count")
    for i in range(count):
        # Gift Sender
        AddLong("AccountId")
        AddLong("CharacterId")
        AddUnicodeString("Name")
        # Gift Receiver
        AddLong("AccountId")
        AddLong("CharacterId")
        AddUnicodeString("Name")
        DecodeGuildBankEntry()
        AddLong("Timestamp")
elif f == 110: # donate
    AddInt("DonationAmount")
    AddLong("DonationTime")
elif f == 114:
    pass # none
elif f == 115:
    f_59_60_115()
elif f == 116:
    AddInt("Unknown")
elif f == 119:
    sub_AE52B0()
    sub_AE52B0()
elif f == 120:
    AddBool("Unknown")
    AddInt("Unknown")

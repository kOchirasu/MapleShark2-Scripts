from script_api import *
from common import *

def f_59_60_115():
    add_bool("Unknown")
    add_bool("Unknown")

def sub_508870():
    add_int("SkillLevel")
    add_int("SkillId (index)")
    add_long("ExpiryTime?")

def sub_AE52B0():
    add_long("Unknown")
    add_unicode_str("UnknownStr")
    add_unicode_str("UnknownStr")
    add_int("Unknown")

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
            add_bool("CanCheckIn?")
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
        add_short("Unknown+151") # 0
        add_unicode_str("MemberProfileUrl")
        add_int("PlotMapId")
        add_int("PlotId") # 41?
        add_int("Unknown+163")
        add_long("PlotExpiration") # By default, but can change...
        for i in range(3):
            add_int("Trophy")

def decode_guild_join_request(): # CGuildJoinRequestForGuild
    with Node("GuildJoinRequest"):
        add_long("Unknown")
        add_long("Unknown")
        add_long("Unknown")
        add_long("Unknown")
        add_unicode_str("UnknownStr")
        add_unicode_str("UnknownStr")
        add_int("Unknown")
        add_int("Unknown")
        add_int("Unknown")
        add_long("Unknown")
    

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
    

def decode_guild_bank_entry():
    with Node("UnknownEntry"):
        add_int("ItemId")
        add_short("Rarity")
        add_int("Amount")
        add_bool("Unknown")
        add_bool("Unknown")
        add_bool("Unknown")
        add_bool("Unknown")


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
    add_byte("Unknown+52")
    add_int("Unknown+53") # 1000
    add_int("Unknown+57")
    add_int("Unknown+61")
    add_int("Unknown+65")
    add_int("Unknown+69")
    add_int("Unknown+73")
    add_int("Unknown+77")
    add_int("Unknown+81")
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
        
    with Node("GuildPosters"):
        add_int("Unknown+131")
        add_int("Unknown+135")
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
            decode_guild_bank_entry()
    
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
elif f == 2: # disband guild
    e = add_byte("Notice") # 0 = success
elif f == 3: # guild invite
    add_unicode_str("Player Name")
elif f == 4:
    decode_guild_invite_info()
elif f == 5: # accepeted to guild
    decode_guild_invite_info()
    add_bool("Notice")
elif f == 6: # invite response msg
    add_unicode_str("PlayerName")
    b = add_byte("Unknown") # T if accept
    add_byte("Notice") # 0=accepted, 1=declined, 2, 3
    if b != 1:
        pass # Display Notice
elif f == 7: # leave guild
    pass # notice
elif f == 8:
    add_unicode_str("UnknownStr")
elif f == 9:
    add_unicode_str("UnknownStr")
elif f == 10: # change player rank
    add_unicode_str("PlayerName")
    add_byte("Rank")
elif f == 11:
    add_unicode_str("UnknownStr")
elif f == 12:
    add_unicode_str("UnknownStr")
    add_unicode_str("UnknownStr")
elif f == 14:
    add_unicode_str("PlayerName")
    add_int("Unknown") # 3382??
elif f == 15: # confirm check in
    pass # none
elif f == 18:
    add_unicode_str("AcceptorName") # maybe leader
    add_unicode_str("PlayerName")
    add_byte("Unknown")
    decode_guild_member()
elif f == 19:
    add_unicode_str("UnknownStr")
elif f == 20: # kicked player
    add_unicode_str("LeaderName")
    add_unicode_str("PlayerName")
elif f == 21: # updated player rank
    add_unicode_str("LeaderName")
    add_unicode_str("PlayerName")
    add_byte("Rank")
elif f == 22: # update motto
    add_unicode_str("PlayerName")
    add_unicode_str("PlayerMotto")
elif f == 23: # guild member logged in
    add_unicode_str("PlayerName")
elif f == 24: # logged off
    add_unicode_str("PlayerName")
    add_long("LogOFfTime?")
elif f == 25: # become leader
    add_unicode_str("OldLeaderName")
    add_unicode_str("NewLeaderName")
elif f == 26: # setting notice
    add_unicode_str("LeaderName")
    add_byte("Notice")
    add_unicode_str("NoticeMessage")
elif f == 27:
    decode_interface_text()
    add_unicode_str("UnknownStr")
elif f == 28:
    add_unicode_str("UnknownStr")
    add_int("Unknown")
elif f == 29: # update rank
    decode_interface_text()
    b = add_bool("Unknown")
    add_int("Unknown")
    if not b:
        add_unicode_str("LeaderName")
    else:
        add_int("Unknown")
        count = add_int("count")
        for i in range(count):
            add_unicode_str("UnknownStr")
    add_byte("Unknown")
    decode_guild_rank()
elif f == 30: # set guild focus msg (???)
    add_unicode_str("LEaderName")
    # guild focus packet
    add_bool("Unkown")
    add_int("FocusFlags")
elif f == 31:
    add_unicode_str("UnknownStr")
    # Some condition
    # add_int("Unknown")
elif f == 32: # update member
    add_unicode_str("PlayerName")
    decode_guild_member_player()
elif f == 33:
    add_unicode_str("UnknownStr")
elif f == 34:
    add_unicode_str("UnknownStr")
elif f == 35:
    add_unicode_str("UnknownStr")
    add_int("Unknown")
    add_int("Unknown")
    add_short("Unknown")
elif f == 36: # sent after updating contribution?
    add_unicode_str("Name")
    add_long("TimeNow")
elif f == 37:
    add_unicode_str("UnknownStr")
    add_int("Unknown")
    add_int("Unknown")
elif f == 38: # CUIService Related
    count = add_int("count")
    for i in range(count):
        add_unicode_str("UnknownStr")
        add_int("Unknown")
        add_int("Unknown")
elif f == 39:
    add_byte("Unknown")
elif f == 40:
    add_byte("Unknown")
elif f == 41:
    add_int("Unknown")
    add_int("Unknown")
    add_int("Unknown")
elif f == 42:
    add_byte("Unknown")
    add_unicode_str("UnknownStr")
elif f == 43:
    add_unicode_str("UnknownStr")
elif f == 44:
    add_unicode_str("UnknownStr")
elif f == 45: # receive application
    decode_guild_join_request()
elif f == 46: # application removed
    add_long("ApplicationUid")
elif f == 47: # accept guild invite
    add_unicode_str("AcceptorName")
    add_unicode_str("AcceptedName")
    add_byte("1 when accepted")
    add_long("ApplicationId")
elif f == 48: # your application rejected
    add_unicode_str("GuildName")
    add_long("ApplicationId")
    add_byte("Unknown") # 0
elif f == 49: # update guild exp
    add_int("GuildExp") # 3307547 (GuildExp?)
elif f == 50: # update guild funds
    add_int("GuildFunds")
elif f == 51: # update contribution
    add_unicode_str("Name")
    add_int("ContributionGained")
    add_int("WeeklyContribution")
    add_int("TotalContribution")
elif f == 52: # Use skill
    add_unicode_str("UsePlayerName")
    sub_508870()
elif f == 53: # skill upgraded
    add_unicode_str("UpgraderName")
    sub_508870()
elif f == 54: # started arcade msg
    add_unicode_str("PlayerName") # who started it
    add_int("GameIndex")
    add_int("timestamp (INT)")
elif f == 55:
    add_unicode_str("UnknownStr")
    add_int("Unknown")
    add_int("Unknown")
elif f == 56:
    add_long("Unknown")
    add_unicode_str("UnknownStr")
    add_int("Unknown")
    add_unicode_str("UnknownStr")
elif f == 57:
    add_unicode_str("UnknownStr")
    # CGuildNpc related
    add_int("Unknown")
    add_int("Unknown")
elif f == 59:
    f_59_60_115()
elif f == 60:
    f_59_60_115()
elif f == 61: # make leader response
    add_unicode_str("NewLeaderName")
elif f == 62: # set guild notice
    add_bool("Unknown") # 1
    add_unicode_str("GuildNotice")
elif f == 63:
    add_unicode_str("UnknownStr")
elif f == 64:
    add_int("Unknown")
elif f == 65: # update rank response
    add_byte("Unknown")
    decode_guild_rank()
elif f == 66: # set guild focus
    add_bool("Unkown")
    add_int("FocusFlags")
elif f == 69: # send mail response
    pass # none
elif f == 72:
    count = add_int("count")
    for i in range(count):
        b = add_bool("flag")
        if b:
            decode_guild_pvp_history_data()
elif f == 73:
    count = add_int("count")
    for i in range(count):
        b = add_bool("flag")
        if b:
            decode_guild_pvp_season_history_data()
elif f == 74:
    count = add_int("count")
    for i in range(count):
        add_unicode_str("UnknownStr")
        add_unicode_str("UnknownStr")
        add_long("Unknown")
elif f == 75: # add guild details above player
    add_unicode_str("PlayerName")
    add_unicode_str("GuildName")
elif f == 76: # left/kicked from guild
    add_unicode_str("Name")
elif f == 77: # create guild name taken
    add_byte("Unknown") # 1
    add_byte("Unknown") # 11
    add_int("Unknown")
elif f == 78:
    add_int("Unknown")
    add_long("Unknown")
    add_long("Unknown")
    add_unicode_str("UnknownStr")
elif f == 80: # apply guild
    add_long("ApplicationId")
    add_unicode_str("GuildName")
elif f == 81: # cancel application
    add_long("ApplicationId")
    add_unicode_str("GuildName")
elif f == 82: # response application
    add_long("ApplicationId")
    add_unicode_str("PlayerName")
    add_bool("IsAccepted") # 0
elif f == 83: # updated players rank?
    count = add_int("count")
    for i in range(count):
        b = add_bool("Unknown")
        if b:
             decode_guild_join_request()
elif f == 84: # load open guild search ui (not in guild)
    count = add_int("count")
    for i in range(count):
        b = add_bool("Requested")
        if b:
            decode_guild_join_requestforchar()
elif f == 85: # Search for guild
    count = add_int("count")
    for i in range(count):
        b = add_bool("Unknown")
        if b:
            decode_search_guild_join()
elif f == 88: # active guild buff
    add_int("GuildBuffId")
elif f == 89: # activate guild personal buff
    add_int("GuildBuffId")
elif f == 95: # acquired guild funds/exp (msg)
    add_int("AcquiredExp")
    add_int("AcquiredFunds")
elif f == 96: # start arcade
    add_int("MinigameIndex")
elif f == 104:
    add_int("Unknown")
elif f == 106:
    b = add_bool("Unknown")
    if not b:
        add_unicode_str("UnknownStr")
elif f == 107: # update gift storage
    # Also causes 0x20 to be sent
    decode_guild_bank_entry()
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
        decode_guild_bank_entry()
        add_long("Timestamp")
elif f == 110: # donate
    add_int("DonationAmount")
    add_long("DonationTime")
elif f == 114:
    pass # none
elif f == 115:
    f_59_60_115()
elif f == 116:
    add_int("Unknown")
elif f == 119:
    sub_AE52B0()
    sub_AE52B0()
elif f == 120:
    add_bool("Unknown")
    add_int("Unknown")

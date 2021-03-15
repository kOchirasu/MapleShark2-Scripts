from script_api import *
from common import *

# Guild
f = AddByte("Function")

if f == 1: # create guild
    AddUnicodeString("GuildName")
elif f == 2: # disband guild
    pass # none
elif f == 3: # guild invite
    AddUnicodeString("PlayerName")
elif f == 5: # accept/decline invite
    DecodeGuildInviteInfo()
    AddBool("IsAccepted")
elif f == 7: # leave guild
    pass # none
elif f == 8: # kick from guild
    AddUnicodeString("PlayerName")
elif f == 10: # change player rank
    AddUnicodeString("PlayerName")
    AddByte("Rank")
elif f == 13: # set motto
    AddUnicodeString("GuildMotto")
elif f == 15: # check-in guild
    pass # none
elif f == 61: # make leader
    AddUnicodeString("NewLeaderName")
elif f == 62: # set guild notice
    AddBool("Unknown") # 1
    AddUnicodeString("GuildNotice")
elif f == 65: # update rank
    AddByte("Unknown")
    DecodeGuildRank()
elif f == 66: # set guild focus
    AddBool("Unkown")
    AddInt("FocusFlags")
elif f == 69: # Send guild mail
    AddUnicodeString("MailTitle")
    AddUnicodeString("MailBody")
elif f == 80: # apply guild
    AddLong("GuildUid")
elif f == 81: # cancel application
    AddLong("ApplicationId")
elif f == 82: # response application
    AddLong("ApplicationUid")
    AddBool("IsAccepted") # false=decline, true=accept
elif f == 83: # sent after changing the players rank
    pass # none
elif f == 84: # load guild search ui (active requests)
    pass # none
elif f == 85: # search for guilds (open ui) by options
    AddInt("Unknown") # bit flags? (-1 default)
    AddInt("Unknown") # 1
elif f == 86: # search by name
    AddUnicodeString("GuildName")
elif f == 88: # active guild buff
    AddInt("GuildBuffId")
elif f == 89: # activate guil personal buff
    AddInt("GuildBuffId")
elif f == 96: # start arcade
    AddInt("MinigameIndex")
elif f == 100: # enter guild house
    pass # none
elif f == 109: # request update gift log
    pass # none (respond 109)
elif f == 110: # donate to guild
    AddInt("DonationCount")

from script_api import *
from common import *

# Guild
f = add_byte("Function")

if f == 1: # create guild
    add_unicode_str("GuildName")
elif f == 2: # disband guild
    pass # none
elif f == 3: # guild invite
    add_unicode_str("PlayerName")
elif f == 5: # accept/decline invite
    decode_guild_invite_info()
    add_bool("IsAccepted")
elif f == 7: # leave guild
    pass # none
elif f == 8: # kick from guild
    add_unicode_str("PlayerName")
elif f == 10: # change player rank
    add_unicode_str("PlayerName")
    add_byte("Rank")
elif f == 13: # set motto
    add_unicode_str("GuildMotto")
elif f == 15: # check-in guild
    pass # none
elif f == 61: # make leader
    add_unicode_str("NewLeaderName")
elif f == 62: # set guild notice
    add_bool("Unknown") # 1
    add_unicode_str("GuildNotice")
elif f == 65: # update rank
    add_byte("Unknown")
    decode_guild_rank()
elif f == 66: # set guild focus
    add_bool("Unkown")
    add_int("FocusFlags")
elif f == 69: # Send guild mail
    add_unicode_str("MailTitle")
    add_unicode_str("MailBody")
elif f == 80: # apply guild
    add_long("GuildUid")
elif f == 81: # cancel application
    add_long("ApplicationId")
elif f == 82: # response application
    add_long("ApplicationUid")
    add_bool("IsAccepted") # false=decline, true=accept
elif f == 83: # sent after changing the players rank
    pass # none
elif f == 84: # load guild search ui (active requests)
    pass # none
elif f == 85: # search for guilds (open ui) by options
    add_int("Unknown") # bit flags? (-1 default)
    add_int("Unknown") # 1
elif f == 86: # search by name
    add_unicode_str("GuildName")
elif f == 88: # active guild buff
    add_int("GuildBuffId")
elif f == 89: # activate guil personal buff
    add_int("GuildBuffId")
elif f == 96: # start arcade
    add_int("MinigameIndex")
elif f == 100: # enter guild house
    pass # none
elif f == 109: # request update gift log
    pass # none (respond 109)
elif f == 110: # donate to guild
    add_int("DonationCount")

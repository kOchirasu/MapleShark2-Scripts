''' RECALL_SCROLL '''
from script_api import *

f = add_byte("function")
notice = add_byte("notice") # 1

if f == 0: # close recall
    pass # none
else: # open recall
    add_unicode_str("PlayerName") # player who used the scroll
    add_int("Unknown") # 1
    add_int("MapId")
    add_int("Unknown") # Random ticks? (Unknown)
    add_long("Timestamp")
    if notice == 0:
        pass # s_cash_recall_guild_notice
    elif notice == 1:
        pass # s_cash_recall_party_notice
    elif notice == 2:
        pass # s_cash_recall_wedding_notice
    else:
        pass # OpenNotify

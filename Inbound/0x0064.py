''' ADMIN_BLOCK '''
from script_api import *

f = add_byte("function")
if f == 0:
    count = add_int("Count")
    for i in range(count):
        add_long("Unknown") # some uid?
        type = add_int("BanType")
        add_long("AccountId")
        add_unicode_str("BlockReason")
        add_long("StartDate")
        add_long("EndDate")
        if type == 2:
            break # s_admin_block_velma_add
        elif type == 4:
            pass # s_admin_block_velma_ugc_add
elif f == 1:
    add_long("unknown") # some uid?
elif f == 2: # change time
    add_long("Unknown") # some uid?
    type = add_int("BanType")
    add_long("AccountId")
    delta = add_int("timeDelta")
    if delta < 0:
        if type == 2:
            pass # s_admin_block_velma_endtime_dec
        elif type == 4:
            pass # s_admin_block_velma_ugc_endtime_dec

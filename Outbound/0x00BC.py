''' WEDDING '''
from script_api import *
from wedding import *

f = add_byte("function")
if f == 3:
    add_unicode_str("unknown")
elif f == 4:
    add_short("unknown")
    add_long("unknown")
elif f == 5:
    add_long("unknown")
elif f == 7:
    pass # s_wedding_divorce_warn
elif f == 9:
    add_short("unknown")
elif f == 13:
    decode_wedding_hall_ticket()
    add_bool("unknown") # true?
elif f == 14:
    add_short("unknown") # (a1 != 0) + 7
elif f == 16:
    pass # WeddingHallModifyLimitHour
elif f == 17:
    add_short("unknown")  # (a1 != 0) + 9
elif f == 18:
    add_short("unknown")  # (a1 != 0) + 9
elif f == 20:
    decode_wedding_hall_ticket()
    # s_wedding_result_err_same_field
elif f == 21:
    add_short("unknown")  # (a1 != 0) + 11
elif f == 26:
    add_long("unknown")
elif f == 27:
    add_unicode_str("unknown")
elif f == 28:
    count = add_int("count")
    for i in range(count):
        add_short("unknown")
        add_long("unknown")
        add_long("unknown")
        add_unicode_str("unknown")
    # s_wedding_result_invitation_send_late
elif f == 30:
    add_byte("unknown") # 3 and var
    add_bool("unknown")
elif f == 34:
    add_unicode_str("unknown")
elif f == 37: # s_wedding_dialog_page_skill_exist
    add_int("unknown")

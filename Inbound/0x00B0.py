''' MY_INFO '''
from script_api import *

add_int("ObjectId")
add_unicode_str("Motto")

n = add_int("unknown")
message = add_unicode_str("message")
if n:
    if message == "":
        pass # s_ban_check_err_any_word
    else:
        pass # MsgBox with message
else:
    pass # UIMyInfoDialog(Motto)

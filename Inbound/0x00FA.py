''' HOME_INVITE '''
from script_api import *

f = add_byte("function")
if f == 0: # Error
    message = add_byte("Message")
    add_unicode_str("Argument")
    if message == 1:
        pass # s_home_invite_accept
    elif message == 2:
        pass # s_home_invite_reject
    elif message == 3:
        pass # s_home_invite_acceptwait
    elif message == 4:
        pass # s_home_invite_logout
    elif message == 5:
        pass # s_home_invite_denybyauto
    elif message == 6:
        pass # s_home_invite_timeout
    elif message == 7:
        pass # s_home_invite_self
    elif message == 9:
        pass # s_home_invite_cant_invite_now
    pass
elif f == 2:
    add_long("unknown")
    add_unicode_str("unknown")
    # Send 0x52 (REQUEST_HOME) function 0
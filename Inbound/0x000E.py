from script_api import *

flag = add_byte("Flag")
if flag == 0:
    add_int("IPAddress")
    add_short("Port")
    add_int("TokenA")
    add_int("TokenB")
    add_int("Map")
else:
    add_unicode_str("StrW")
if flag == 49:
    ParseLong("[2]")

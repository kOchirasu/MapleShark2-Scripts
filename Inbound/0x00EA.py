from script_api import *

f = add_byte("function")
if f == 0:
    add_unicode_str("Unknown")
    add_int("Unknown")
elif f == 1:
    add_int("NpcObjectId")
    add_unicode_str("Unknown")
elif f == 2:
    add_int("NpcObjectId")
    add_unicode_str("Unknown")
elif f == 3:
    add_byte("Unknown")
    add_int("duration")
    add_str("Unknown")
    add_str("illust")
    add_str("sound")
    add_str("Unknown")
    add_unicode_str("message")

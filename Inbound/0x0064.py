from script_api import *

f = add_byte("function")
if f == 0:
    count = add_int("Count")
    for i in range(count):
        add_long("Unknown")
        add_int("BanType?")
        add_long("AccountId")
        add_unicode_str("BlockReason")
        add_long("StartDate")
        add_long("EndDatei")

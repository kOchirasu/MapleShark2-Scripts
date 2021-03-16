from script_api import *

add_byte("state") # 0x00 = success, 0x07 = restricted, 0x19 = timed out
add_int("Unknown")
add_unicode_str("BanReason")
add_long("AccountId")
add_long("SyncTime")
add_int("SyncTicks")
add_byte("TimeZone")
f = add_byte("function")
add_int("CONST (0)")
add_long("CONST (0)")
if f == 1:
    add_long("Timestamp")
elif f == 2:
    add_long("Timestamps")
    add_long("CurrentTimestamp")
add_int("2 (CONST)")

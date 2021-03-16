from script_api import *

# Exp up
f = add_byte("Function")
if f == 0:
    # [00] [5A 16 02 00 00 00 00 00] 23 04 5C 3C 1A 00 00 00 00 00 5E 94 89 01 00 00 00 00 00 00 00 00 00
    add_long("GainedExp")
    add_short("UnknownSeeSendMoney")
    add_long("CurrentExp")
    add_long("RestExp?")
    add_int("Unknown")
    add_bool("Unknown")
elif f == 1:
    add_long("RestExp?")

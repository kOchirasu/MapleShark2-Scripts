from script_api import *

# Exp up
f = AddByte("Function")
if f == 0:
    # [00] [5A 16 02 00 00 00 00 00] 23 04 5C 3C 1A 00 00 00 00 00 5E 94 89 01 00 00 00 00 00 00 00 00 00
    AddLong("GainedExp")
    AddShort("UnknownSeeSendMoney")
    AddLong("CurrentExp")
    AddLong("RestExp?")
    AddInt("Unknown")
    AddBool("Unknown")
elif f == 1:
    AddLong("RestExp?")

from script_api import *

# First packet sent on handshake in some cases
AddByte("function") # 0
count = AddInt("Unknown")
for i in range(count):
    AddUnicodeString("UnknownStr")
    AddLong("Unknown")

from script_api import *


AddByte("Unknown (1)")
AddInt("Unknown (1)")
AddUnicodeString("Server Name")
AddByte("Unknown (4)")
count = AddShort("count")
for i in range(count):
    AddUnicodeString("IPAddress")
    AddShort("Port")

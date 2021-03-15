from script_api import *

flag = AddByte("Flag")
if flag == 0:
    AddInt("IPAddress")
    AddShort("Port")
    AddInt("TokenA")
    AddInt("TokenB")
    AddInt("Map")
else:
    AddUnicodeString("StrW")
if flag == 49:
    ParseLong("[2]")

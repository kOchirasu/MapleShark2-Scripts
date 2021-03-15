from script_api import *


f = AddByte("Function")
if f == 17:
    AddUnicodeString("Endpoint 1")
    AddUnicodeString("Endpoint 2")
    AddUnicodeString("Locale")
    AddByte("const")
elif f == 22:
    AddInt("const")

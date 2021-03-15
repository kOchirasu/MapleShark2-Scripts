from script_api import *

f = AddByte("Function")

if f == 0:
    count = AddInt("count")
    for i in range(count):
        with Node("Entry " + str(i)):
            #AddUnicodeString("UnknownStr")
            # Data Depends on string
            pass
elif f == 1:
    pass
elif f == 2:
    pass
elif f == 3:
    pass

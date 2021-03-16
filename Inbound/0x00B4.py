from script_api import *

f = add_byte("Function")

if f == 0:
    count = add_int("count")
    for i in range(count):
        with Node("Entry " + str(i)):
            #add_unicode_str("UnknownStr")
            # Data Depends on string
            pass
elif f == 1:
    pass
elif f == 2:
    pass
elif f == 3:
    pass

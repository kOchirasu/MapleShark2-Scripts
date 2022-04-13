''' SERVER_LIST '''
from script_api import *

# sub_E08310
b = add_bool("load servers")
if b:
    add_int("Unknown (1)")
    add_unicode_str("Server Name")
    add_byte("Unknown (4)")
    count = add_short("count")
    for i in range(count):
        add_unicode_str("IPAddress")
        add_short("Port")

    add_int("unknown (100)")
    with Node("CMultiServerChannel", True):
        count = add_short("count")
        for i in range(count):
            add_int("channel")

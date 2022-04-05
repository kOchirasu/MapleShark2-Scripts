''' SERVER_LIST (incomplete - virtual calls?) '''
from script_api import *


add_bool("success")
add_int("Unknown (1)")
add_unicode_str("Server Name")
add_byte("Unknown (4)")
count = add_short("count")
for i in range(count):
    add_unicode_str("IPAddress")
    add_short("Port")

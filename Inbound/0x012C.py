''' WEDDING_BILLBOARD '''
from script_api import *
from wedding import *

f = add_byte("function")
if f == 4:
    count = add_int("count")
    for i in range(count):
        add_long("unknown")
        decode_wedding_hall_ticket()

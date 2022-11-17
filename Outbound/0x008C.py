''' ITEM_SOCKET_SCROLL '''
from script_api import *

f = add_byte("function")
if f == 1:
    add_long("itemUid")
    add_long("scrollUid")

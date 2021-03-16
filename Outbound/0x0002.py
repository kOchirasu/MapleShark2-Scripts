from script_api import *

# First packet sent on handshake in some cases
add_byte("function") # 0
count = add_int("Unknown")
for i in range(count):
    add_unicode_str("UnknownStr")
    add_long("Unknown")

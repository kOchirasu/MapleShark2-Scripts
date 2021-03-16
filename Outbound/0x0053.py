from script_api import *

add_unicode_str("Name")
add_unicode_str("Message")

f = add_byte("function")
if f == 0: # reporting player
    add_int("Unknown") # 1
elif f == 1: # reporting chat
    add_int("Unknown")
    add_unicode_str("UnknownStr")
elif f == 2: # reporting poster
    add_int("Unknown")
    add_long("Unknown")
    add_unicode_str("UnknownStr")
elif f == 3: # reporting design item
    add_int("Unknown")
    add_long("Unknown")
elif f == 4: # reporting real estate item (house)
    add_int("Bit-flag of reasons")
    add_long("PlayerId")
    add_int("Unknown") # 0
    add_int("Unknown") #0
elif f == 7: # reporting pet
    add_int("Unknown")

"""
add_byte("Unknown")
add_byte("Unknown")
add_long("Unknown")
add_long("Unknown")
add_unicode_str("UnknownStr")
add_unicode_str("UnknownStr")
add_long("Unknown")
add_str("UnknownStr")
add_unicode_str("UnknownStr")
add_long("Unknown")
add_long("Unknown")
add_str("UnknownStr")
add_int("Unknown")
add_long("Unknown")
"""

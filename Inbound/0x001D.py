from script_api import *

add_long("AccountId")
add_long("CharacterId")
add_unicode_str("Name")
add_byte("Unknown")
add_unicode_str("Message")
msgType = add_int("Type")
add_byte("Unknown")
add_int("Channel")
if msgType == 3:
    add_unicode_str("UnknownStr")
elif msgType == 16:
    add_int("ItemId?")
elif msgType == 20:
    add_long("CharacterId?")
add_byte("Unknown")

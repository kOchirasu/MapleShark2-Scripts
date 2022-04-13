''' USER_CHAT '''
from script_api import *

add_long("AccountId")
add_long("CharacterId")
add_unicode_str("Name")
add_byte("Unknown")
add_unicode_str("Message")
msgType = add_int("Type")
add_byte("Unknown")
add_int("Channel")
if msgType == 3: # whisper from
    add_unicode_str("UnknownStr")
elif msgType == 16: # super chat
    add_int("SuperChatItemId")
elif msgType == 20: # club chat
    add_long("ClubUid")
add_byte("Unknown")

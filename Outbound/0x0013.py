''' EMOTE '''
from script_api import *

f = add_byte("Function")
if f == 1: # LearnEmote
    add_long("ItemUid")
elif f == 2: # UseEmote
    add_int("emoteId")
    add_unicode_str("emotion")
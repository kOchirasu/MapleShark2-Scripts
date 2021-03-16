from script_api import *

f = add_byte("function")

if f == 1: # user recall portal
    add_unicode_str("PlayerName") # player who used the scroll
    add_int("MapId")

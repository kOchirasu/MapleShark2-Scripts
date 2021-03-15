from script_api import *

f = AddByte("function")

if f == 1: # user recall portal
    AddUnicodeString("PlayerName") # player who used the scroll
    AddInt("MapId")

from script_api import *

f = AddByte("function")
if f == 1: # create group
    AddUnicodeString("Unknown")
elif f == 2: # invite player
    AddUnicodeString("UserName")
    AddInt("GroupChatId")
elif f == 4: # leave group
    AddInt("GroupChatId")
    AddBool("Unknown") # 0
elif f == 10: # message group
    AddUnicodeString("Message")
    AddInt("GroupChatId")

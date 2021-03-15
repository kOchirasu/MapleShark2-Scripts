from script_api import *
from common import *

f = AddByte("function")
if f == 0: # create group #1
    AddInt("GroupChatId")
    count = AddByte("count")
    for i in range(count):
        t = AddByte("Type?")
        if t == 1 or t ==2:
            DecodePlayer()
elif f == 1: # create group #2
    AddInt("GroupChatId")
elif f == 2: # invite #1
    AddUnicodeString("InviteSender")
    AddUnicodeString("InvitedPlayer")
    AddInt("GroupChatId")
elif f == 3: # receive invite
    AddUnicodeString("InviteSender")
    AddUnicodeString("InvitedPlayer")
    AddInt("GroupChatId")
elif f == 4: # left group (self)
    AddInt("GroupChatId")
elif f == 6: # invite #2
    AddInt("Unknown")
    AddUnicodeString("OwnerName")
    t = AddByte("Type?")
    if t == 1 or t ==2:
        DecodePlayer()
elif f == 7: # player left group (others)
    AddInt("GroupChatId")
    AddByte("Unknown")
    AddUnicodeString("Name")
elif f == 8:
    AddInt("GroupChatId")
    AddUnicodeString("Unknown")
elif f == 9:
    AddInt("GroupChatId")
    AddUnicodeString("Unknown")
elif f == 10: # message group
    AddInt("GroupChatId")
    AddUnicodeString("UserName")
    AddUnicodeString("Message")
elif f == 11:
    AddInt("GroupChatId")
    AddUnicodeString("Unknown")
elif f == 12:
    AddInt("GroupChatId")
    AddUnicodeString("Unknown")
    AddUnicodeString("Unknown")
elif f == 13:
    AddByte("Unknown")
    AddInt("GroupChatId")
    AddUnicodeString("Unknown")
    AddUnicodeString("Unknown")

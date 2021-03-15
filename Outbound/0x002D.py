from script_api import *

f = AddByte("function")

if f == 0: # load mail
    pass # none
elif f == 1: # send mail
    AddUnicodeString("Recipient")
    AddUnicodeString("Title")
    AddUnicodeString("Message")
elif f == 2: # view unread mail
    AddLong("MailUid")
elif f == 11: # collect one item (AddToInventory + MarkNew)
    AddLong("MailUid")
elif f == 13: # delete mail
    count = AddInt("count")
    for i in range(count):
        AddLong("MailUid")
elif f == 18: # mark read
    count = AddInt("count")
    for i in range(count):
        AddLong("MailUid")
elif f == 19: # collect multiple mail
    count = AddInt("count")
    for i in range(count):
        AddLong("MailUid")

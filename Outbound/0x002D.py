from script_api import *

f = add_byte("function")

if f == 0: # load mail
    pass # none
elif f == 1: # send mail
    add_unicode_str("Recipient")
    add_unicode_str("Title")
    add_unicode_str("Message")
elif f == 2: # view unread mail
    add_long("MailUid")
elif f == 11: # collect one item (AddToInventory + MarkNew)
    add_long("MailUid")
elif f == 13: # delete mail
    count = add_int("count")
    for i in range(count):
        add_long("MailUid")
elif f == 18: # mark read
    count = add_int("count")
    for i in range(count):
        add_long("MailUid")
elif f == 19: # collect multiple mail
    count = add_int("count")
    for i in range(count):
        add_long("MailUid")

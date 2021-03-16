from script_api import *
from common import *

f = add_byte("function")

if f == 0: # load mail
    count = add_int("count")
    for i in range(count):
        with Node("MailEntry " + str(i), True):
            n = add_byte("UnknownNum") # 102
            add_long("MailUid") # 59030013
            add_long("SenderCharacterId") # SomeUid
            # <ms2><v key="s_blackmarket_mail_to_sender" /></ms2>
            add_unicode_str("SenderName")
            # <ms2><v key="s_blackmarket_mail_to_buyer_title" /></ms2>
            add_unicode_str("MailTitle")
            # <ms2><v key="s_blackmarket_mail_to_buyer_content" /></ms2>
            add_unicode_str("MailContent")
            # <ms2><v item="30000235" ></v></ms2>
            add_unicode_str("MetadataKey")
            # Purchase 10 for 60 total, 6 each
            # <ms2><v item="30000235" ></v><v str="10" ></v><v money="60" ></v><v money="6" ></v></ms2>
            add_unicode_str("MetadataValue")
            if n == 200: # CMailAdItem
                adCount = add_byte("AdCount")
                for j in range(adCount):
                    add_int("Unknown")
                    add_int("Unknown")
                    add_int("Unknown")
                    add_int("Unknown")
                    add_long("Unknown")
                    add_long("Unknown")
                    add_long("Unknown")
                add_unicode_str("UnknownStr")
                add_long("Unknown")
                add_byte("Unknown")
            else: # CMailAttachItem
                itemCount = add_byte("ItemCount")
                for j in range(itemCount):
                    with Node("AttachedItem " + str(j)):
                        id = add_int("ItemId")
                        add_long("ItemUid")
                        add_byte("Unknown")
                        add_int("Rarity")
                        add_int("Amount")
                        add_long("Unknown")
                        add_int("Unknown")
                        add_long("Unknown")
                        decode_item(id)
            add_long("Unknown")
            add_long("Unknown")
            add_long("Unknown")
            add_long("Unknown")
            add_long("Unknown")
            add_long("Unknown")
            count2 = add_byte("Count")
            for j in range(count2):
                add_byte("Unknown")
                add_byte("Unknown")
                add_long("Unknown")
                add_long("Unknown")
            add_long("ViewedTime")
            add_long("ExpiryTime")
            add_long("SentTime")
            add_unicode_str("UnknownStr")
elif f == 1: # send custom mail confirm
    add_long("MailUid")
elif f == 2: # mark mail viewed
    add_long("MailUid")
    add_long("ViewedTime") # Now
elif f == 3: # error
    add_long("Unknown")
elif f == 10: # collecting mail #1
    add_long("MailUid")
    add_byte("Unknown") # 1
    add_byte("Unknown") # 0
    add_long("CollectTime")
elif f == 11: # collecting mail #2
    add_long("MailUid")
    add_long("ViewedTime")
elif f == 12:
    add_long("Unknown")
    add_long("Unknown")
elif f == 13: # delete mail
    add_long("MailUid")
elif f == 14: # receive mail
    add_int("UnreadMailCount")
    add_bool("Unknown") # 1
    add_int("Unknown")
elif f == 15:
    pass # none
elif f == 16: # start list
    pass # none
elif f == 17: # end list
    pass # none
elif f == 20: # switch (error)
    add_byte("Unknown") # used in default case
    add_byte("ErrorCode")
elif f == 22:
    add_unicode_str("UnknownStr")
    add_byte("Unknown")
    add_int("Unknown")
    add_byte("Unknown")
    add_int("Unknown")
    add_str("UnknownStrA")
    add_unicode_str("UnknownStr")

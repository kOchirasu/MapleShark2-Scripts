from script_api import *
from common import *

f = AddByte("function")

if f == 0: # load mail
    count = AddInt("count")
    for i in range(count):
        with Node("MailEntry " + str(i), True):
            n = AddByte("UnknownNum") # 102
            AddLong("MailUid") # 59030013
            AddLong("SenderCharacterId") # SomeUid
            # <ms2><v key="s_blackmarket_mail_to_sender" /></ms2>
            AddUnicodeString("SenderName")
            # <ms2><v key="s_blackmarket_mail_to_buyer_title" /></ms2>
            AddUnicodeString("MailTitle")
            # <ms2><v key="s_blackmarket_mail_to_buyer_content" /></ms2>
            AddUnicodeString("MailContent")
            # <ms2><v item="30000235" ></v></ms2>
            AddUnicodeString("MetadataKey")
            # Purchase 10 for 60 total, 6 each
            # <ms2><v item="30000235" ></v><v str="10" ></v><v money="60" ></v><v money="6" ></v></ms2>
            AddUnicodeString("MetadataValue")
            if n == 200: # CMailAdItem
                adCount = AddByte("AdCount")
                for j in range(adCount):
                    AddInt("Unknown")
                    AddInt("Unknown")
                    AddInt("Unknown")
                    AddInt("Unknown")
                    AddLong("Unknown")
                    AddLong("Unknown")
                    AddLong("Unknown")
                AddUnicodeString("UnknownStr")
                AddLong("Unknown")
                AddByte("Unknown")
            else: # CMailAttachItem
                itemCount = AddByte("ItemCount")
                for j in range(itemCount):
                    with Node("AttachedItem " + str(j)):
                        id = AddInt("ItemId")
                        AddLong("ItemUid")
                        AddByte("Unknown")
                        AddInt("Rarity")
                        AddInt("Amount")
                        AddLong("Unknown")
                        AddInt("Unknown")
                        AddLong("Unknown")
                        DecodeItem(id)
            AddLong("Unknown")
            AddLong("Unknown")
            AddLong("Unknown")
            AddLong("Unknown")
            AddLong("Unknown")
            AddLong("Unknown")
            count2 = AddByte("Count")
            for j in range(count2):
                AddByte("Unknown")
                AddByte("Unknown")
                AddLong("Unknown")
                AddLong("Unknown")
            AddLong("ViewedTime")
            AddLong("ExpiryTime")
            AddLong("SentTime")
            AddUnicodeString("UnknownStr")
elif f == 1: # send custom mail confirm
    AddLong("MailUid")
elif f == 2: # mark mail viewed
    AddLong("MailUid")
    AddLong("ViewedTime") # Now
elif f == 3: # error
    AddLong("Unknown")
elif f == 10: # collecting mail #1
    AddLong("MailUid")
    AddByte("Unknown") # 1
    AddByte("Unknown") # 0
    AddLong("CollectTime")
elif f == 11: # collecting mail #2
    AddLong("MailUid")
    AddLong("ViewedTime")
elif f == 12:
    AddLong("Unknown")
    AddLong("Unknown")
elif f == 13: # delete mail
    AddLong("MailUid")
elif f == 14: # receive mail
    AddInt("UnreadMailCount")
    AddBool("Unknown") # 1
    AddInt("Unknown")
elif f == 15:
    pass # none
elif f == 16: # start list
    pass # none
elif f == 17: # end list
    pass # none
elif f == 20: # switch (error)
    AddByte("Unknown") # used in default case
    AddByte("ErrorCode")
elif f == 22:
    AddUnicodeString("UnknownStr")
    AddByte("Unknown")
    AddInt("Unknown")
    AddByte("Unknown")
    AddInt("Unknown")
    AddString("UnknownStrA")
    AddUnicodeString("UnknownStr")

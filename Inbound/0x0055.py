''' MAIL '''
from script_api import *
from common import *

def decode_mail_ad_item(): # sub_005B6670
    add_int("Unknown")
    add_int("Unknown")
    add_int("Unknown")
    add_int("Unknown")
    add_long("Unknown")
    add_long("Unknown")
    add_long("Unknown")

def decode_mail_attach_item():
    id = add_int("ItemId")
    add_long("ItemUid")
    add_byte("Index")
    add_int("Rarity")
    add_int("Amount")
    add_long("Unknown")
    add_int("Unknown")
    add_long("Unknown")
    decode_item(id)

def decode_mail_info():
    type = add_byte("type") # 102
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
    if type == 200: # CMailAdItem
        adCount = add_byte("AdCount")
        for j in range(adCount):
            with Node("AdItem " + str(j)):
                decode_mail_ad_item()
        add_unicode_str("UnknownStr")
        add_long("Unknown")
        add_byte("Unknown")
    else: # CMailAttachItem
        itemCount = add_byte("ItemCount")
        for j in range(itemCount):
            with Node("AttachedItem " + str(j)):
                decode_mail_attach_item()
    add_long("Unknown")
    add_long("Unknown")
    add_long("Unknown")
    add_long("Unknown")
    add_long("Unknown")
    add_long("Unknown")

    # sub_45E8C0
    count2 = add_byte("Count")
    for j in range(count2):
        add_byte("Unknown")
        add_byte("Unknown")
        add_long("Unknown")
        add_long("Unknown")
    # end sub

    add_long("ViewedTime")
    add_long("ExpiryTime")
    add_long("SentTime")
    add_unicode_str("UnknownStr")
    if type == 3 or type == 103 or type == 107 or type == 109 or type == 111:
        pass # do something special?
    if type - 1 > 0:
        pass # do something
    if type == 3 or type == 100 or type == 103:
        pass # do something special? -> ReadXml...


f = add_byte("function")
if f == 0: # load mail
    count = add_int("count")
    for i in range(count):
        with Node("MailInfo " + str(i), True):
            decode_mail_info()
elif f == 1: # send custom mail confirm
    add_long("MailUid") # is this true? I don't see it in IDA
    pass # s_mail_send
elif f == 2: # readMail
    add_long("MailUid")
    add_long("ViewedTime") # Now
elif f == 3: # error
    add_long("Unknown")
    # s_mail_return
elif f == 10: # collecting mail #1
    add_long("MailUid")
    add_bool("Unknown") # 1
    # below is only used if above is true
    add_byte("Unknown") # 0, assert(<= 4)
    add_long("CollectTime")
elif f == 11: # collecting mail #2
    add_long("MailUid")
    add_long("ViewedTime")
elif f == 12:
    add_long("MailUid")
    add_long("Timestamp")
elif f == 13: # delete mail
    add_long("MailUid")
elif f == 14: # receive mail
    add_int("UnreadMailCount")
    add_bool("Unknown") # 1
    add_int("count")
    # s_notify_mail_recieve
elif f == 15:
    pass # s_mail_period_item_include, s_mail_period_item_include_chat
elif f == 16: # start list
    pass # none
elif f == 17: # end list
    pass # none
elif f == 20: # switch (error)
    add_byte("Unknown") # used in default case
    message = add_byte("message")
    '''
    if message == 1:
        pass # s_mail_error_username
    elif message == 2 or message == 5:
        pass # s_mail_error_attachcount
    elif message == 3 or message == 4:
        pass # s_mail_error_cannot_attach_item
    elif message == 12:
        pass # s_mail_error_sendmail
    elif message == 16:
        pass # s_mail_error_alreadyread
    elif message == 17:
        pass # s_mail_error_already_receive
    elif message == 20:
        pass # s_mail_error_attachcount + effect(17)
    elif message == 21:
        pass # s_mail_error_already_receive
    elif message == 22:
        pass # s_mail_error_attachcount + effect(18)
    elif message == 23:
        pass # s_mail_error_ad_expired
    elif message == 24:
        pass # s_mail_error_createmail
    elif message == 25:
        pass # s_mail_error_recipient_equal_sender
    elif message == 26:
        pass # s_err_lack_meso
    elif message == 27:
        pass # s_mail_error_block_from_me
    elif message == 28:
        pass # s_mail_error_block_from_other
    elif message == 29:
        pass # s_mail_error_admin_character
    elif message == 30:
        pass # s_mail_error_from_admin_to_user
    elif message == 31:
        pass # s_mail_error_bancheck
    elif message == 32:
        pass # s_mail_error_admin_block
    elif message == 33:
        pass # s_anti_addiction_cannot_receive
    else:
        pass # s_mail_error
    '''
elif f == 22:
    add_unicode_str("UnknownStr")
    add_byte("Unknown")
    add_int("Unknown")
    add_byte("Unknown")
    add_int("Unknown")
    add_str("UnknownStrA")
    add_unicode_str("UnknownStr")
    # s_mail_notify_recieve_gift, s_mail_get_gift_item

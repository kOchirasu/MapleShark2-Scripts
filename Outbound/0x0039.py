'''UGC'''
from script_api import *


def decode_ugc_reserve(n: int):
    with Node("CUgcBannerPostReserve " + str(n)):
        add_long("uuid")
        add_int("2")
        add_long("Banner id")
        add_int("Date")
        add_int("Hour")
        add_long("0")

def decode_ugc_info():
    type = add_byte("UGC Type")
    add_byte("Unk")
    add_byte("Unk")
    add_int("Unk")
    add_long("Account ID")
    add_long("Character ID")
    return type

f = add_byte("Function")
if f == 1: #create ugc
    add_long("Unk")
    type = decode_ugc_info()
    add_long("Unk")
    add_int("Unk")
    add_short("Unk")
    add_short("-256")
    if type == 1 or type == 2 or type == 7: # item, furniture and mount
        add_long("Uid")
        add_int("Item ID")
        add_int("Amount")
        add_unicode_str("Item Name")
        add_byte("Unk")
        add_long("Cost")
        add_bool("Use voucher")
    elif type == 3: #banners
        add_long("Banner id")
        hours = add_byte("Hours")
        for i in range(hours):
            decode_ugc_reserve(i)
elif f == 3: #confirmation (?)
    type = decode_ugc_info()
    add_int("Unk")
    add_long("UGC Uid")
    add_unicode_str("UGC Guid")
    add_short("-255")
elif f == 18: #load banners
    add_int("Map id")
elif f == 19: #reserve banner
    add_long("Banner id")
    hours = add_int("Hours")
    for i in range(hours):
        decode_ugc_reserve(i)
'''UGC'''
from script_api import *

def decode_ugc_reserve():  # CUgcBannerReserve
    add_long("Banner id")
    hours = add_int("Hour count")
    for x in range(hours):
        with Node("Hour " + str(x)):
            add_long("Uid")
            add_int("1")
            add_long("Banner ID")
            add_int("Date")
            add_int("Hour")
            add_long("unk")

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
    if type == 1 or type == 2: # item and furniture
        add_long("Uid")
        add_int("Item ID")
        add_int("Amount")
        add_unicode_str("Item Name")
        add_byte("Unk")
        add_long("Cost")
        add_bool("Use voucher")
    elif type == 3: #banners
        decode_ugc_reserve()
elif f == 3: #confirmation (?)
    type = decode_ugc_info()
    add_int("Unk")
    add_long("UGC Uid")
    add_unicode_str("UGC Guid")
    add_short("-255")
elif f == 18: #load banners
    add_int("Map id")
elif f == 19: #reserve banner
    decode_ugc_reserve()
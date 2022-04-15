''' UGC '''
from script_api import *
from common import *

def decode_ugc_item(): # CUgcItemProxy
    with Node("CUgcItemProxy"):
        add_long("unknown")
        add_int("unknown")
        add_int("unknown")
        add_byte("unknown")
        add_long("unknown")
        add_float("unknown")

def decode_ugc_blueprint_image(): # CUgcBlueprintImageProxy
    with Node("CUgcBlueprintImageProxy"):
        add_long("unknown")
        add_long("unknown")
        add_int("unknown")
        add_unicode_str("unknown")

def decode_ugc_banner_rolling_image(): # CUgcBannerRollingImage
    with Node("CUgcBannerRollingImage"):
        add_long("unknown")
        add_unicode_str("unknown")
        add_byte("unknown")
        add_int("unknown")
        add_long("unknown")
        add_long("unknown")
        add_unicode_str("unknown")
        add_unicode_str("unknown")
        add_unicode_str("unknown")

def decode_ugc_banner_post(): # CUgcBannerPost
    with Node("CUgcBannerPost"):
        # valid: 0,1,2,3,4,5,6,7,8,9,10,201,202,209 others cause exception
        add_byte("type")
        with Node("CUgcUserProxy"):
            add_int("unk")
            add_long("Account ID")
            add_long("Character ID")
            add_unicode_str("unk")
            add_unicode_str("Character Name")
        with Node("CUgcUploadProxy"):
            add_long("UGC Uid")
            add_unicode_str("UGC GUID")
            add_byte("unk")
            add_byte("unk")
        add_long("Banner id")
        count = add_byte("Hour count")
        for i in range(count):
            with Node("CUgcBannerPostReserve " + str(i)):
                add_long("uuid")
                add_int("2")
                add_long("Banner id")
                add_int("Date")
                add_int("Hour")
                add_long("0")
        add_unicode_str("UGC url")

def decode_ugc_hour_post():
    add_long("Date + Hour")
    add_unicode_str("Character name")
    add_byte("Reserved")

def decode_ugc_reserve(): # CUgcBannerReserve
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

f = add_byte("Function")
if f == 0:
    pass
if f == 2: # create UGC
    add_byte("UGC Type")
    # if type is invalid -> invaild ugcType
    add_long("UGC Uid")
    add_unicode_str("UGC Guid")
    # error PreUpload
    # error soap upload
elif f == 4: # set url
    add_byte("UGC Type")
    add_long("UGC Uid")
    # return codes 13=err, 91, 92
    add_unicode_str("UGC Url")
elif f == 6:
    add_long("unknown")
    count = add_int("count")
    for i in range(count):
        add_long("unknown")
elif f == 7:
    add_long("unknown")
    n = add_byte("unknown")
    if n == 1:
        decode_ugc_banner_post()
elif f == 8: #update banner
    add_long("Banner id")
    hours = add_int("Hours")
    for x in range(hours):
        with Node("Hour " + str(x)):
            decode_ugc_hour_post()
elif f == 11:
    add_int("unknown")
    add_long("unknown")
    add_unicode_str("unknown")
elif f == 13 or f == 14 or f == 15:
    add_int("unknown")
    decode_ugc_item()
    decode_ugc_data()
elif f == 16:
    add_int("unknown")
    decode_ugc_blueprint_image()
    decode_ugc_data()
elif f == 17:
    add_unicode_str("Endpoint 1")
    add_unicode_str("Endpoint 2")
    add_unicode_str("Locale")
    add_byte("unknown") # const?
elif f == 18: #load banners
    count = add_int("count")
    for i in range(count):
        b = add_bool("unknown")
        if b:
            decode_ugc_banner_rolling_image()
    count = add_int("count2")
    for x in range(count):
        bannerId = add_long("Banner id")
        with Node("Banner " + str(bannerId)):
            active = add_byte("Active")
            if active:
                decode_ugc_banner_post()
    count3 = add_int("count3")
    for x in range(count3):
        decode_ugc_reserve()
elif f == 20: #init ugc creation
    decode_ugc_reserve()
elif f == 21:
    count = add_int("count")
    for i in range(count):
        add_long("unknown")
        add_int("unknown")
elif f == 22:
    add_int("unknown") # const?

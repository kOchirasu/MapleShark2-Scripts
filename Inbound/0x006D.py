''' UGC '''
from script_api import *
from item import *

def decode_ugc_item(): # CUgcItemProxy
    with Node("CUgcItemProxy"):
        add_long("Item UID")
        add_int("Item ID")
        add_int("Item Amount")
        add_unicode_str("Item Name")
        add_byte("const 1")
        add_long("Item Sale Price")
        add_bool("unknown")

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
        count = add_byte("Hours")
        for i in range(count):
            decode_ugc_reserve(i)
        add_unicode_str("UGC url")

def decode_ugc_reserve(n: int):
    with Node("CUgcBannerPostReserve " + str(n)):
        add_long("uuid")
        add_int("2")
        add_long("Banner id")
        add_int("Date")
        add_int("Hour")
        add_long("0")

def decode_ugc_hour_post():
    add_long("Date + Hour")
    add_unicode_str("Character name")
    add_byte("Reserved")

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
    for i in range(hours):
        with Node("Hour " + str(i)):
            decode_ugc_hour_post()
elif f == 11:
    add_int("unknown")
    add_long("unknown")
    add_unicode_str("unknown")
elif f == 13 or f == 14 or f == 15:
    add_int("Player Object ID")
    decode_ugc_item()
    decode_ugc_item_look()
elif f == 16:
    add_int("unknown")
    decode_ugc_blueprint_image()
    decode_ugc_item_look()
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
    count = add_int("count")
    for i in range(count):
        bannerId = add_long("Banner id")
        with Node("Banner " + str(bannerId)):
            active = add_byte("Active")
            if active:
                decode_ugc_banner_post()
    count = add_int("count")
    for i in range(count):
        bannerId = add_long("Banner id")
        with Node("Banner " + str(bannerId)):
            hours = add_int("Hour count")
            for j in range(hours):
                with Node("Hour " + str(j)):
                    decode_ugc_hour_post()
elif f == 20:  # CUgcPreReserve
    add_long("Banner id")
    hours = add_int("Hours")
    for i in range(hours):
        decode_ugc_reserve(i)
elif f == 21:  # CUgcGetCostTable
    count = add_int("count")
    for i in range(count):
        add_long("unknown")
        add_int("unknown")
elif f == 22:
    add_int("unknown") # const?

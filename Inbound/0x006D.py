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
        add_unicode_str("unknown")

def decode_ugc_unknown():
    add_unicode_str("unknown")
    add_byte("unknown")

def decode_ugc_reserve(): # CUgcBannerReserve
    add_long("unknown")
    count = add_int("count")
    for i in range(count):
        add_int("unknown")
        add_long("unknown")
        add_int("unknown")
        add_int("unknown")
        add_long("unknown")

f = add_byte("Function")
if f == 0:
    pass
elif f == 2:
    add_byte("ugcType")
    # if type is invalid -> invaild ugcType
    add_long("unknown")
    add_unicode_str("unknown")
    # error PreUpload
    # error soap upload
elif f == 4:
    add_byte("ugcType")
    add_long("unknown")
    # return codes 13=err, 91, 92
    add_unicode_str("unknown")
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
elif f == 8:
    add_long("unknown")
    count = add_int("count")
    for i in range(count):
        add_long("unknown")
        decode_ugc_unknown()
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
elif f == 18:
    count = add_int("count")
    for i in range(count):
        b = add_bool("unknown")
        if b:
            decode_ugc_banner_rolling_image()
    count = add_int("count")
    for i in range(count):
        b = add_bool("unknown")
        add_long("unknown")
        if b:
            decode_ugc_banner_post()
    count = add_int("count")
    for i in range(count):
        add_int("unknown")
        add_long("unknown")
        decode_ugc_unknown()
elif f == 20:
    decode_ugc_reserve()
elif f == 21:
    count = add_int("count")
    for i in range(count):
        add_long("unknown")
        add_int("unknown")
elif f == 22:
    add_int("unknown") # const?

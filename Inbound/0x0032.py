''' BEAUTY '''
from script_api import *
from common import *

def decode_cost():
    with Node("TShopPaymentAttr", True):
        add_byte("CurrencyType") # 0 = mesos, 9 = meret, 1 = custom?
        add_int("CurrencyItemId")
        add_int("Amount")
        add_str("UnknownStr+52")

def decode_shop():
    with Node("Shop", True):
        add_byte("BeautyCategory") # 1 = Standard, 2 = Special, 3 = Dye, 4 = Save
        add_int("ShopId")
        add_int("BeautyType") # 1-Hair, 3-Face, 4-Skin, 5-Dye
        add_int("VoucherItemId")
        add_bool("UseCustomCurrency")
        add_int("CurrencyId")
        add_int("ShopIndex???")
        add_bool("Unknown+31")
        decode_cost()
        decode_cost()


f = add_byte("Function")
# UIBeautyShopDialog
if f == 0: # load beauty shop
    decode_shop()
    add_byte("Unknown+54")
    add_byte("Unknown+55")
    count = add_short("count")
    for i in range(count):
        with Node("CBeautyShopItem " + str(i)):
            add_int("CosmeticId")
            add_byte("ShopItemBanner") # 1 = New, 2 = Event, 3 = Half Price, 4 = Special
            add_short("RequiredLevel") # 0
            add_int("AchievmentId")
            add_byte("AchievementRank")
            decode_cost()
elif f == 1: # load dye shop
    decode_shop()
    add_byte("Unknown+54")
    add_byte("Unknown+55")
    add_unicode_str("UnknownStr")
elif f == 3:
    add_int("Unknown")
elif f == 4:
    add_long("Unknown")
elif f == 5:
    add_long("Unknown")
    add_int("Unknown")
elif f == 7:
    add_long("Unknown")
    add_int("Unknown")
elif f == 8:
    message = add_int("message")
    if message == 2:
        pass # sub_D32A00 has random different errors
    elif message == 12:
        pass # STYLESHOP: s_beauty_msg_error_style_slot_extend_max
    elif message == 11: 
        pass # s_beauty_msg_error_color
    elif message == 17:
        pass # break
    elif message == 18:
        pass # s_beauty_msg_error_style_slot_max
    elif message == 19:
        pass # s_cannot_charge_merat
    elif message == 22:
        pass # STYLESHOP: s_beauty_msg_error_style_disable_gender
    elif message == 23:
        pass # STYLESHOP: s_beauty_msg_error_style_apply_already
    elif message == 24:
        pass # STYLESHOP: s_beauty_msg_error_style_save_cant_not_beauty_day
    else:
        pass # s_beauty_msg_error_code
elif f == 9: # useVoucher
    add_int("ItemId")
    add_int("Amount")
elif f == 11: # random hair option
    add_int("PreviousHairItemId")
    add_int("NewHairItemId")
elif f == 12: # choose random hair
    message = add_int("message")
    b = add_bool("success")
    if message == 0:
        pass # s_beauty_msg_complete_apply_special_hair
    else:
        if b:
            pass # s_beauty_msg_complete_apply_return_coupon_to_mail
        else:
            pass # s_beauty_msg_complete_apply_return_coupon
''' Skipping this StyleShop handler
elif f == 16 or f == 17:
    pass # s_beauty_msg_complete_save_hair_style
'''


# UIBeautyShopStyleDialog
if f == 2: # load save shop
    decode_shop()
    add_byte("Unknown+54")
    add_byte("Unknown+55")
    add_unicode_str("UnknownStr")
elif f == 13: # initialize saved hairs ?
    pass # payback related?
elif f == 14: # load saved hair count
    add_short("Haircount")
elif f == 15: # load saved hairs
    count = add_short("count")
    for i in range(count):
        with Node("Hair " + str(i)):
            id = add_int("ItemId")
            add_long("ItemUid")
            add_int("slot")
            add_long("CreationTime")
            decode_equip_color()
            add_int("AppearanceFlag")
            add_field("Back Hair Position", 4 * 7)
            add_field("Front Hair Position", 4 * 7)
elif f == 16 or f == 17: # save hair
    add_long("HairUid")
    add_long("SaveUid")
    add_byte("Index?")
    add_long("Timesaved")
elif f == 18: # delete hair: s_beauty_msg_complete_remove_saved_hair_style
    add_long("SaveUid")
elif f == 20: # load save window: s_beauty_msg_complete_extend_style_slot
    add_byte("Unknown")
    add_short("Unknown")
elif f == 21: # change to saved hair
    pass # s_beauty_msg_complete_apply_saved_style
from script_api import *
from common import *

def decode_cost():
    with Node("Cost?", True):
        add_byte("CurrencyType") # 0 = mesos, 9 = meret, 1 = custom?
        add_int("CurrencyItemId") # if type == 1?
        add_int("Amount")
        add_str("UnknownStr+52")


f = add_byte("Function")
if f == 0:
    add_byte("Unknown+9")
    add_int("ShopId")
    add_int("Unknown+14") # 1-Hair, 3-Face, 4-Skin, 5-Dye
    add_int("VoucherItemId")
    add_byte("UseCustomCurrency")
    add_int("CurrencyId")
    add_int("ShopIndex???")
    add_byte("Unknown+31")
    decode_cost()
    decode_cost()
    add_byte("Unknown+54")
    add_byte("Unknown+55")
    count = add_short("count")
    for i in range(count):
        with Node("Option " + str(i)):
            add_int("CosmeticId")
            add_bool("IsNew")
            add_short("Unknown+63") # 0
            add_int("AchievmentId")
            add_byte("AchievementRank")
            decode_cost()
elif f == 1:
    add_byte("Unknown+9")
    add_int("ShopId")
    add_int("Unknown+14")
    add_int("VoucherItemId")
    add_byte("Unknown+22")
    add_int("Unknown+23")
    add_int("Unknown+27")
    add_byte("Unknown+31")
    decode_cost()
    decode_cost()
    add_byte("Unknown+54")
    add_byte("Unknown+55")
    add_unicode_str("UnknownStr")
elif f == 2:
    add_byte("Unknown+9")
    add_int("ShopId")
    add_int("Unknown+14")
    add_int("VoucherItemId")
    add_byte("Unknown+22")
    add_int("Unknown+23")
    add_int("Unknown+27")
    add_byte("Unknown+31")
    decode_cost()
    decode_cost()
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
    add_int("Unknown+9")
elif f == 9: # useVoucher
    add_int("ItemId")
    add_int("Amount")
elif f == 14:
    add_short("Unknown+9")
elif f == 15:
    count = add_short("count")
    for i in range(count):
        with Node("Hair " + str(i)):
            id = add_int("ItemId")
            add_long("ItemUid")
            add_int("Unknown+23")
            add_long("CreationTime")
            decode_equip_color()
            add_int("AppearanceFlag")
            add_field("Back Hair Position", 4 * 7)
            add_field("Front Hair Position", 4 * 7)
elif f == 16: # Saved Hair
    add_long("HairUid")
    add_long("SaveUid")
    add_byte("Index?")
    add_long("Timesaved")
elif f == 18: # delete hair
    add_long("SaveUid")
elif f == 20:
    add_byte("Unknown")
    add_short("Unknown")

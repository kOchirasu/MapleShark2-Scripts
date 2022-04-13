from script_api import *
from common import *

f = add_byte("Function")
if f == 0: # load shop
    add_int("NpcId")
    add_byte("BeautyCategory") # 1 = standard, 2 = special, 3 = dye, 4 = save
elif f == 3: # new beauty
    add_byte("Index?")
    add_byte("UseVoucher") # sub_821610
    add_int("BeautyItemShopId")
    # Might not be hair here
    decode_equip_color()
    add_int("AppearanceFlag")
    add_field("Back Hair Position", 4 * 7)
    add_field("Front Hair Position", 4 * 7)
elif f == 4: 
    add_long("Unknown")
elif f == 5: # change hair/eyes color
    add_byte("Index?") # Since it's hair color, no style here?
    add_byte("UseVoucher") # sub_821610
    add_long("HairUid")
    decode_equip_color()
    add_int("AppearanceFlag")
    add_field("Back Hair Position", 4 * 7)
    add_field("Front Hair Position", 4 * 7)
elif f == 6: # change skin color
    add_byte("Index?")
    decode_skin_color()
    add_byte("UseVoucher") # sub_821610
elif f == 7: # randomize hair
    add_int("ShopId")
    add_bool("UseVoucher")
elif f == 10: # teleport
    add_short("Type") # 1 = beauty salon, 3 = plastic surgey, 5 = dye workshop
elif f == 12:
    add_byte("Unknown")
elif f == 16: # save hair
    add_long("HairUid")
elif f == 18: # delete hair
    add_long("SaveUid")
    add_bool("True")
elif f == 22: # gear dye
    count = add_byte("count")
    for i in range(count):
        with Node("Item " + str(i)):
            add_short("Quantity")
            add_bool("UseVoucher")
            add_field("Unknown", 13)
            add_long("ItemUid")
            add_int("ItemId")
            decode_equip_color()
            add_int("AppearanceFlag")
elif f == 23: # use beauty voucher
    add_long("itemUid")

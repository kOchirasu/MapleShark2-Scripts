''' BEAUTY '''
from script_api import *
from item import *

f = add_byte("Function")
if f == 0: # load shop
    add_int("NpcId")
    add_byte("BeautyCategory") # 1 = standard, 2 = special, 3 = dye, 4 = save
elif f == 3: # new beauty
    add_byte("Index?")
    add_byte("UseVoucher") # sub_821610
    add_int("BeautyItemShopId")
    decode_item_extra_data(HAIR_ID)
elif f == 4: 
    add_long("ItemUid")
elif f == 5: # change hair/eyes color
    add_byte("Index?") # Since it's hair color, no style here?
    add_byte("UseVoucher") # sub_821610
    add_long("HairItemUid")
    decode_item_extra_data(HAIR_ID)
elif f == 6: # change skin color
    add_byte("Index?")
    decode_skin_color()
    add_byte("UseVoucher") # sub_821610
elif f == 7: # randomize hair
    add_int("ShopId")
    add_bool("UseVoucher")
elif f == 10: # teleport
    # s_beauty_goto_map_return_warn
    add_short("Type") # 1 = beauty salon, 3 = plastic surgey, 5 = dye workshop
elif f == 12: # OnClickRandomSelect
    add_byte("Unknown")
elif f == 16: # onClickSaveCurStyle => s_beauty_msg_error_style_slot_max_in_style_npc/s_beauty_msg_ask_save_style_extend_in_style_npc
    add_long("ItemUid")
elif f == 17: # s_beauty_msg_ask_save_style_extend_in_style_npc, s_beauty_msg_error_style_slot_max
    add_long("ItemUid")
elif f == 18: # s_beauty_msg_ask_delete_style
    add_long("ItemUid")
    add_bool("True")
elif f == 19:
    pass # s_beauty_msg_ask_save_style_extend
elif f == 21:
    add_long("ItemUid")
    add_byte("Slot")
elif f == 22: # gear dye
    count = add_byte("count")
    for i in range(count):
        with Node("Item " + str(i)):
            add_short("Quantity")
            add_bool("UseVoucher")
            add_field("Unknown", 13)
            add_long("ItemUid")
            id = add_int("ItemId")
            decode_item_extra_data(id)
elif f == 23: # use beauty voucher
    add_int("unknown")
    add_long("itemUid")

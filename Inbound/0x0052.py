''' SHOP '''
from script_api import *
from common import *

def decode_buy_period():
    b = add_bool("Unknown")
    if b:
        add_long("Unknown")
        add_long("Unknown")
    b = add_bool("Unknown")
    if b:
        count = add_byte("count")
        for i in range(count):
            add_int("Unknown")
            add_int("Unknown")
        count = add_byte("count")
        for i in range(count):
            add_byte("Unknown")

def decode_shop_item():
    add_int("serialId")
    id = add_int("ItemId")
    add_byte("field_64") # CurrencyType?
    add_int("CurrencyId")
    add_int("field_6C") # 0
    add_int("Price")
    add_int("SomeOtherPrice") # unknown
    add_byte("Rarity")
    add_int("random num") # item related, used to initialize
    add_int("MaxStock") # 0 = infinite
    add_int("TotalSold")
    add_int("field_3C")
    add_str("ShopCategory")
    add_int("AchievmentRequired")
    add_int("field_44")
    add_byte("field_48")
    add_short("field_4C")
    add_byte("field_50")
    add_short("field_54")
    add_bool("field_60") # false
    add_short("bundleSize?") # 1
    add_byte("field_90") # 1
    add_byte("field_94") # 1 (Has currency id str?)
    add_str("CurrencyIdStr")
    add_short("field_58")
    add_int("field_5C")
    add_bool("Unknown")
    b = add_bool("hasBuyPeriod") # CNpcShopBuyPeriod
    if b:
        decode_buy_period()
    decode_item(id)

def decode_meret_premium_item():
    with Node("CMeratMarketPremiumProduct"): # sub_5C29D0
        # sub_5BD390
        add_int("unknown")
        add_byte("unknown")
        add_unicode_str("unknown")
        add_byte("unknown")
        add_int("unknown")
        add_int("unknown")
        add_byte("unknown")
        add_byte("unknown")
        add_byte("unknown")
        add_long("unknown")
        add_long("unknown")
        add_byte("unknown")
        add_int("unknown")
        add_int("unknown")
        add_byte("unknown")
        add_int("unknown")
        add_byte("unknown")
        add_short("unknown")
        add_short("unknown")
        add_int("unknown")
        add_int("unknown")
        add_byte("unknown")
        add_int("unknown")
        add_int("unknown")
        add_int("unknown")
        add_int("unknown")
        add_int("unknown")
        add_int("unknown")
        add_byte("unknown")
        add_bool("unknown")
        add_int("unknown")
        # n == 1 -> # sub_5C2770, n == 3 -> sub_5C28A0 (both seem to decode same though...)
        # CDBPremiumProduct
        count = add_byte("count")
        for i in range(count):
            b = add_bool("b")
            if b: # sub_5BCDD0
                add_int("unknown")
                add_byte("unknown")
                add_unicode_str("unknown")
                add_byte("unknown")
                add_int("unknown")
                add_int("unknown")
                add_int("unknown")
                add_byte("unknown")
                add_byte("unknown")
                add_byte("unknown")
                add_long("unknown")
                add_long("unknown")
                add_byte("unknown")
                add_long("unknown")
                add_long("unknown")
                add_int("unknown")
                add_int("unknown")
                add_byte("unknown")
                add_int("unknown")
                add_byte("unknown")
                add_short("unknown")
                add_short("unknown")
                add_int("unknown")
                add_int("unknown")
                add_byte("unknown")
                add_int("unknown")
                add_int("unknown")
                add_int("unknown")
                add_int("unknown")
                add_int("unknown")
                add_byte("unknown")
                add_int("unknown")
                add_str("unknown")
                add_str("unknown")
                add_bool("unknown")
                add_byte("unknown")
                add_int("unknown")
                add_bool("unknown")
                add_int("unknown")
                add_int("unknown")
                add_int("unknown")
                add_byte("unknown")
                add_bool("unknown")
                add_int("unknown")
                b = add_bool("unknown")
                if b:
                    add_str("unknown")
                    add_long("unknown")
                    add_long("unknown")
                add_byte("unknown")
                add_bool("unknown")

# 05 6E 9F D4 DB 71 98 CB 27 87 00 00 00 [f] [uid] [amount] (sell item)
# 03 01 00 00 00 [f] [index] (rebuy)
f = add_byte("function") # compared against ShopObj+13C also

if f == 0: # Start load shop
    add_int("NpcId")
    add_int("ShopId")
    add_long("ResetTime")
    add_int("RemainSeconds")
    add_short("ItemCount")
    add_int("field_204") # 5
    add_byte("Unknown+35")
    add_bool("field_213")
    canRestock = add_bool("CanRestock") # button for restocking
    add_bool("field_215")
    add_byte("type_sub_E15470")
    add_bool("field_210")
    add_bool("field_211")
    add_bool("field_212")
    add_bool("field_213")
    add_str("shopName")
    if canRestock:
        add_byte("field_21C")
        add_byte("field_220")
        add_int("field_224")
        add_int("InstantRestockCost")
        add_bool("field_238")
        add_int("field_23C")
        add_byte("shopType") # important
        add_bool("field_240")
        add_bool("field_241")
elif f == 1: # add shop item (CNpcShopProductCli)
    count = add_byte("count")
    for i in range(count):
        with Node("Item " + str(i), i == 0):
            decode_shop_item()
elif f == 2: # ITEM_UPDATE
    add_int("serialId")
    add_int("buyCount")
elif f == 4: # ITEM_BUY
    add_int("ItemId")
    buyCount = add_int("buyCount")
    add_int("TotalPrice")
    add_byte("fontColor?") # sub_CD0F60, only used for GuildStorage
    b = add_bool("ToGuildStorage")
    if b:
        if buyCount <= 1:
            pass # s_msg_take_item_to_guild_storage
        else:
            pass # s_msg_take_item_count_to_guild_storage
elif f == 6: # end load shop
    add_short("Unknown") # 1
elif f == 7: # ITEM_REPURCHASE_ADD
    count = add_short("count")
    for i in range(count):
        add_int("serialId") # nRepurchaseID
        id = add_int("ItemId")
        add_byte("Rarity")
        add_long("Price")
        decode_item(id)
elif f == 8: # ITEM_REPURCHASE_REMOVE
    add_int("serialId") # nRepurchaseID
elif f == 9: # pay for restock, response
    b = add_bool("restock")
    if b:
        add_int("unknown") # used for string table lookup
        add_int("unknown") # used for string table lookup
        # s_shop_reset_refund_item
elif f == 11:
    add_short("unknown")
elif f == 12:
    count = add_byte("count")
    for i in range(count): # CNpcShopMeratItemCli
        with Node("MeratItem " + str(i)):
            decode_meret_premium_item()
            add_byte("unknown")

            add_int("unknown")
            add_int("unknown")
elif f == 13:
    add_int("NpcId")
    add_int("ShopId")
    # if NpcId and ShopId are valid
    add_int("field_208")
    add_short("field_24C")
elif f == 14: # CNpcShopProductNewCli
    count = add_byte("count")
    for i in range(count): # CNpcShopItemNew
        itemId = add_int("ItemId")
        add_bool("field_10")
        add_byte("Rarity")
        add_str("field_18") # delimited
        add_byte("field_1C")
        add_byte("field_20")
        b = add_bool("hasBuyPeriod")
        if b:
            decode_buy_period()
        decode_item(itemId)
elif f == 15:
    message = add_int("message")
    add_byte("unknown") # compared against ShopObj+13C
    stringId = add_int("stringId") # only used for case 10
    '''
    if message == 2 or message == 12:
        pass # s_err_lack_shopitem
    elif message == 4 or message == 5 or message == 6:
        pass # s_err_invalid_item
    elif message == 7 or message == 8 or message == 28:
        pass # no message
    elif message == 9:
        pass # s_msg_cant_sell
    elif message == 10:
        pass # stringId message
    elif message == 11:
        pass # s_err_lack_merat
    elif message == 14:
        pass # s_err_inventory
    elif message == 15:
        pass # s_err_lack_guild_trophy
    elif message == 17:
        pass # s_err_lack_payment_item
    elif message == 19:
        pass # s_err_lack_guild_require_date
    elif message == 22:
        pass # s_anti_addiction_cannot_receive
    elif message == 23:
        pass # s_msg_cant_sell_to_only_sell_shop
    elif message == 24:
        pass # s_word_trade, s_system_property_protection_time
    elif message == 25:
        pass # s_guild_err_buy_no_master
    elif message == 26:
        pass # s_char_ask_delete_confirm_checkbox
    elif message == 27:
        pass # s_err_invalid_item_cannot_buy_by_period
    elif message == 29:
        pass # s_shop_no_star_point_event
    elif message == 30:
        pass # s_shop_err_change_reset_price
    elif message == 31:
        pass # s_meratmarket_error_country_limit
    elif message == 32:
        pass # s_err_cannot_sell_petitem_summon
    else:
        pass # s_item_err_code
    '''

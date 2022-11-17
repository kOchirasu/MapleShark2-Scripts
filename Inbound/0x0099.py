''' ITEM_ENCHANT '''
from script_api import *
from item import *

f = add_byte("Function")
if f == 5:
    # Start enchanting?
    enchantType = add_short("EnchantType") # 1 = Ophelia, 2 = Peachy
    # Some condition or else: stop here
    add_long("ItemUid")

    count = add_byte("IngredientInfoCount")
    for i in range(count):
        with Node("IngredientInfo"):
            add_int("Unknown")
            add_int("RequiredItem (DiffId)") # 100 = crytal frag, 101 = onyx, 102 = chaos
            add_int("Amount")

    add_short("Unknown+1D4")

    count = add_int("Count")
    for i in range(count):
        add_short("StatType")
        decode_stat_option(i)

    if enchantType == 1:
        add_float("SuccessRate") # 100
        add_float("UnknownRate2")
        add_float("UnknownRate3")
        add_float("CatalystTotalRate")
        add_float("ChargeTotalRate")
        add_long("Unknown")
        add_long("Unknown")
        #add_byte("Unknown")
    # Required item copies
    if enchantType == 1 or enchantType == 2:
        add_int("ItemId")
        add_short("Rarity")
        add_int("Amount")
elif f == 6: # This is sent with peachy
    add_long("ItemUid")
    add_int("EnchantExp") # progress related for peachy
elif f == 7:
    add_int("ChargeCount")
    add_int("CatalystWeight") # Toad's Toolkit may count as 2
    count = add_int("CatalystCount")
    for i in range(count):
        add_long("CatalystItemUid")
    add_float("SuccessRate") # 100
    add_float("UnknownRate2")
    add_float("UnknownRate3")
    add_float("CatalystTotalRate")
    add_float("ChargeTotalRate")
elif f == 8: # prop, updateEnchantIngredient
    add_int("CatalystWeight")
    count = add_int("Count")
    for i in range(count):
        add_long("CatalystItemUid")
elif f == 9:
    pass # s_itemenchant_enchant_exp_refund_ok, Send_ItemEnchant(op=1)
elif f == 10:
    add_long("ItemUid")
    decode_item(0) # Don't know ItemId
    # Bonus from enchanting (e.g. 2% def)
    count = add_int("Count")
    for i in range(count):
        add_short("StatType")
        decode_stat_option(i)
elif f == 11:
    add_long("ItemUid")
    decode_item(0) # Don't know ItemId

    add_int("Unknown")
    add_int("Unknown")
    add_long("Unknown")
    add_int("FailStacks")
elif f == 12: # Error
    code = add_short("Code")
    if code == 1:
        pass # s_itemenchant_invalid_item
    elif code == 2:
        pass # s_itemenchant_damaged_item
    elif code == 3:
        pass # s_itemenchant_lack_ingredient
    else:
        pass # s_itemenchant_unknown_err
elif f == 15:
    add_long("ItemUid")
elif f == 16:
    pass
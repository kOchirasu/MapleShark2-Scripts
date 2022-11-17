''' ENCHANT_SCROLL '''
from script_api import *
from item import *

f = add_byte("Function")
if f == 0:
    add_long("itemUid")
    type = add_short("type")
    add_bool("untradeable notice")
    add_int("EnchantLevel")
    add_int("Rate * 10000") # Divided by 100, Rate?
    add_short("MinLevel")
    add_short("MaxLevel")
    count = add_int("item type ecount")
    for _ in range(count):
        add_int("item type")
    count = add_int("rarity count")
    for _ in range(count):
        add_int("rarity")
    if type == 3: # Random enchant
        add_int("MinEnchant")
        add_int("MaxEnchant")
elif f == 1:
    add_long("itemUid")
    type = add_short("type")
    if type == 1 or type == 2:
        count = add_int("Count")
        for _ in range(count):
            add_short("StatType")
            add_float("rate")
            add_int("value")
    elif type == 3:
        count = add_int("Count")
        for _ in range(count):
            add_short("StatType")
            add_float("MinRate")
            add_int("MinValue")
        count = add_int("Count")
        for _ in range(count):
            add_short("StatType")
            add_float("MaxRate")
            add_int("MaxValue")
    elif type == 5:
        pass
elif f == 3: # Error
    message = add_short("message")
    if message == 0: # s_enchantscroll_ok
        add_long("unknown")
        decode_item(0)
    elif message == 1:
        pass # s_enchantscroll_invalid_scroll
    elif message == 2:
        pass # s_enchantscroll_invalid_item
    elif message == 3:
        pass # s_enchantscroll_breaking_item
    elif message == 4:
        pass # s_enchantscroll_invalid_level
    elif message == 5:
        pass # s_enchantscroll_invalid_slot
    elif message == 6:
        pass # s_enchantscroll_invalid_rank
    elif message == 7:
        pass # s_enchantscroll_invalid_grade
    elif message == 8:
        pass # s_enchantscroll_not_breaking_item
elif f == 4: # reward
    count = add_int("count")
    for _ in range(count):
        add_int("id")
        add_short("type?")

''' ITEM_FUSION '''
from script_api import *

def decode_item_merge_option(): # CItemMergeOptionProxy
    add_long("ItemUid")
    add_int("unknown")
    count = add_int("count")
    for i in range(count):
        add_int("unknown")
    
    # CItemMergeOptionVariation
    count = add_int("count")
    for i in range(count):
        add_short("unknown")
        add_int("unknown")
        add_int("unknown")
        add_float("unknown")
        add_float("unknown")

    # CItemMergeOptionVariation
    count = add_int("count")
    for i in range(count):
        add_short("unknown")
        add_int("unknown")
        add_int("unknown")
        add_float("unknown")
        add_float("unknown")


f = add_byte("function")
if f == 0: # UIItemMergeOptionDialog: setSelectItem
    count = add_int("count")
    for i in range(count):
        add_long("ItemUid")
elif f == 1: # UIItemMergeOptionDialog
    count = add_int("count")
    for i in range(count):
        decode_item_merge_option()
elif f == 3: # UIItemMergeOptionDialog
    n = add_short("unknown")
    if n == 0:
        add_long("unknown")
elif f == 4: # UIDTEventDialog
    add_long("ItemUid")
    # virtual function call v19+16
    # s_item_merge_option_revert

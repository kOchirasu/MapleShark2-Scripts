from script_api import *

f = add_byte("function")

if f == 1: # confirm put item
    add_long("ItemUid")
    add_short("slot")
    add_int("Amount")
elif f == 2: # confirm remove item
    add_long("ItemUid")
elif f == 3: # dismantle results
    add_byte("Unknown")
    count = add_int("count")
    for i in range(count):
        with Node("Item " + str(i), True):
            add_int("ItemId")
            add_int("Amount")
elif f == 5: # preview dismantle results
    count = add_int("count")
    for i in range(count):
        with Node("Item " + str(i), True):
            add_int("ItemId")
            add_int("amount min")
            add_int("amount max")

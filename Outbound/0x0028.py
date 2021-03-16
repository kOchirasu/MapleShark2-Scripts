from script_api import *

f = add_byte("function")

if f == 2: # buy item
    add_int("ShopItemId")
    add_int("Amount")
elif f == 9: # pay for restock
    add_int("restock price")
elif f == 10: # Times up restock
    pass
from script_api import *

f = AddByte("function")

if f == 2: # buy item
    AddInt("ShopItemId")
    AddInt("Amount")
elif f == 9: # pay for restock
    AddInt("restock price")
elif f == 10: # Times up restock
    pass
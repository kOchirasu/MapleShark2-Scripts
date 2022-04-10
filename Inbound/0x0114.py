from script_api import *

f = add_byte("function")

if f == 0: # select super chat theme
    add_int("ObjectId")
    add_int("ItemId")
if f == 1: # deselect
    add_int("ObjectId")
from script_api import *
from item import *

f = add_byte("function")
if f == 0:
    add_long("CharacterId")
    add_short("Unknown") # 01 00
elif f == 1:
    add_byte("Gender")
    add_short("JobCode")
    add_unicode_str("Name")
    decode_skin_color()
    add_field("Unknown", 2)
    count = add_byte("count")
    for i in range(count):
        id = add_int("ItemId")
        add_unicode_str("EquipSlot")
        decode_item_extra_data(id)
    add_int("Unknown")
elif f == 2: # delete
    add_long("CharacterId")
elif f == 3: # cancel delete
    add_long("CharacterId")

from script_api import *
from common import *

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
        decode_equip_color()
        add_int("AppearanceFlag")
        # Item positioning
        if id / 100000 == 113:
            add_field("Cap Position", 13 * 4)
        elif id / 100000 == 102:
            add_field("Back Hair Position", 4 * 7)
            add_field("Front Hair Position", 4 * 7)
        elif id / 100000 == 104:
            add_field("Cosmetic Position", 4 * 4)
    add_int("Unknown")
elif f == 2: # delete
    add_long("CharacterId")
elif f == 3: # cancel delete
    add_long("CharacterId")

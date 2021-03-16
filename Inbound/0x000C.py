from script_api import *
from common import *

def decode_list_entry():
    decode_player()

    add_unicode_str("same char profile url")
    add_long("???")

    # This is bugged for some equip types
    count = add_byte("EQUIPMENT")
    for j in range(count):
        with Node("Item " + str(j)):
            id = add_int("Id")
            add_long("Uid")
            equipType = add_unicode_str("Type")
            add_int("??? ^" + str(equipType))
            decode_item(id)

    with Node("Badges"):
        count = add_byte("count")
        for j in range(count):
            with Node("Badge " + str(j)):
                add_byte("???")
                id = add_int("ItemId")
                add_long("Unknown")
                add_int("Unknown")
                decode_item(id)

    b = add_bool("???")
    if b:
        add_long("???")
        add_long("???")
        b = add_bool("flag?")
        if b:
            add_int("???")
            add_long("???")
            add_unicode_str("WStrA")
            add_int("???")

f = add_byte("Function")
if f == 0:
    charCount = add_byte("Count")
    for i in range(charCount):
        decode_list_entry()
elif f == 1:
    decode_list_entry()
elif f == 2: # delete from list
    add_int("Unknown")
    add_long("characterId")
elif f == 5: # delete pending
    add_long("characterId")
    add_int("Unknown")
    add_long("DeleteTime")
elif f == 6: # delete cancel
    add_long("characterId")
    add_int("Unknown")

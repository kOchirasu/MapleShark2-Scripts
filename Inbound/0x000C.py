''' CHARACTER_LIST '''
from script_api import *
from common import *

def delete_message(message):
    if message == 0:
        pass # requestDelete
    elif message == 1:
        pass # s_char_err_already_destroy
    elif message == 2:
        pass # s_char_err_exist_ugc_map
    elif message == 3:
        pass # s_char_err_guild_master
    elif message == 4:
        pass # s_char_err_guild
    elif message == 5:
        pass # s_char_err_ugc_market
    elif message == 6:
        pass # s_char_err_black_market_count
    elif message == 7:
        pass # s_char_err_unread_mail
    elif message == 8:
        pass # s_char_err_no_destroy_wait
    elif message == 9:
        pass # s_char_err_meso_market_count
    elif message == 10:
        pass # s_char_err_next_delete_char_date
    elif message == 11:
        pass # s_char_err_wedding
    else:
        pass # s_char_err_destroy

def decode_list_entry():
    decode_player()

    add_unicode_str("same char profile url")
    add_long("???")

    # This is bugged for some equip types
    count = add_byte("EQUIPMENT")
    for j in range(count):
        with Node("Item " + str(j)):
            id = add_int("ItemId")
            add_long("ItemUid")
            equipType = add_unicode_str("Slot Type")
            add_int("rarity ^" + str(equipType))
            decode_item(id)

    with Node("Badges"):
        count = add_byte("count")
        for j in range(count):
            with Node("Badge " + str(j)):
                add_byte("slot")
                id = add_int("ItemId")
                add_long("ItemUid")
                add_int("rarity")
                decode_item(id)

    # Outfit with stats
    hasSkin2 = add_bool("HasSkin2")
    if hasSkin2:
        add_long("???")
        add_long("???")
        count = add_byte("StatOutfits")
        for j in range(count):
            id = add_int("ItemId")
            add_long("ItemUid")
            equipType = add_unicode_str("Slot Type")
            add_int("rarity ^" + str(equipType))
            decode_item(id)

f = add_byte("Function")
if f == 0: # load character list
    charCount = add_byte("Count")
    for i in range(charCount):
        decode_list_entry()
elif f == 1: # add to list
    decode_list_entry()
elif f == 2: # delete from list
    add_int("Unknown")
    add_long("characterId")
elif f == 3:
    pass
elif f == 4:
    add_byte("unknown")
elif f == 5: # delete pending
    add_long("characterId")
    message = add_int("messageId")
    add_long("DeleteTime")
    #delete_message(message)
elif f == 6: # cancel delete
    add_long("characterId")
    message = add_int("messageId")
    #delete_message(message)
elif f == 7: # change name
    f = add_int("confirm")
    if f == 1:
        pass # s_change_charname_disconnect

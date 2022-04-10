from script_api import *

f = add_byte("Function")

if f == 0: # load chat stickers
    count = add_short("Favorite Sticker Count")
    for i in range(count):
        add_int("StickerId")
    count = add_short("Chat Sticker Count")
    for i in range(count):
        add_int("Sticker Group Id")
        add_long("ExpirationTimestamp")
elif f == 1: # expired sticker notification
    add_int("Unknown")
    count = add_long("StickersCount")
    for i in range(count):
        add_int("StickerGroupId")
elif f == 2: # add sticker
    add_int("Item Id")
    add_int("QuantityGuess")
    add_int("StickerGroupId")
    add_long("ExpirationTimestamp")
elif f == 3: # use sticker
    add_int("Sticker Id")
    add_unicode_str("Script") # html of sticker
    add_byte("Unknown")
elif f == 4: # group chat sticker
    add_int("StickerId")
    add_unicode_str("GroupChatName")
elif f == 5: # favorite
    add_int("StickerId")
elif f == 6: # unfavorite
    add_int("StickerId")
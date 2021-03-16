from script_api import *
from common import *

def decode_script_content():
    add_unicode_str("Unknown")
    add_unicode_str("Unknown")
    add_unicode_str("Unknown")

def decode_cinematic_content():
    decode_script_content()
    add_int("Unknown")
    n = add_byte("Unknown")

    if n == 1:
        count = add_byte("Unknown") # OR *(v2 + 4)
        for i in range(count):
            add_unicode_str("Unknown")
            add_unicode_str("Unknown")
            add_unicode_str("Unknown")


f = add_byte("Function")
# f == 0: Cancel
if f == 1:
    add_int("ObjectId")
    add_byte("TypeFlags") # 2?
    add_int("ScriptId")
    add_int("ScriptIndex") # when there's mutliple parts to a scriptId
    add_int("Options") # Affects selections...
elif f == 2 or f == 8: # continue talking
    add_byte("TypeFlags")
    add_int("Unknown")
    add_int("ScriptId")
    add_int("ScriptIndex")
    add_int("Options")
elif f == 3:
    f = add_byte("Function")
    if f == 1:
        add_unicode_str("UnknownStr")
        # add_short("Short / X")
    elif f == 3: # Move PC
        add_int("SomeLocaionId")
    elif f == 4:
        add_unicode_str("UnknownStr") # BeautyShopDialog
        add_unicode_str("UnknownStr") # itemcolor
    elif f == 5:
        count = add_int("count")
        for i in range(count):
            id = add_int("ItemId")
            add_byte("Unknown") # 1
            add_int("Unknown") # 1
            decode_item(id)
    elif f == 6:
        add_long("Unknown")
    elif f == 7:
        add_long("Unknown")
    elif f == 8:
        add_int("Unknown")
    elif f == 9:
        add_int("Unknown")
        add_byte("Unknown")
    elif f == 10:
        add_int("Unknown")
        add_unicode_str("Unknown")
elif f == 9:
    add_byte("Unknown")
    add_int("Unknown")
    add_int("Unknown")
    add_int("Unknown")
elif f == 10:
    add_int("Unknown")
    add_short("Unknown") # some type
    add_int("Unknown")
    add_byte("Unknown")
    add_int("Unknown")
    add_byte("Unknown")
    count = add_int("Unknown")
    for i in range(count):
        t = add_byte("ScriptType")
        if t == 1: # CChatBalloonContent
            decode_script_content()
        else:
            decode_cinematic_content()

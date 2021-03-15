from script_api import *
from common import *

def DecodeCScriptContent():
    AddUnicodeString("Unknown")
    AddUnicodeString("Unknown")
    AddUnicodeString("Unknown")

def DecodeCCinematicContent():
    DecodeCScriptContent()
    AddInt("Unknown")
    n = AddByte("Unknown")

    if n == 1:
        count = AddByte("Unknown") # OR *(v2 + 4)
        for i in range(count):
            AddUnicodeString("Unknown")
            AddUnicodeString("Unknown")
            AddUnicodeString("Unknown")


f = AddByte("Function")
# f == 0: Cancel
if f == 1:
    AddInt("ObjectId")
    AddByte("TypeFlags") # 2?
    AddInt("ScriptId")
    AddInt("ScriptIndex") # when there's mutliple parts to a scriptId
    AddInt("Options") # Affects selections...
elif f == 2 or f == 8: # continue talking
    AddByte("TypeFlags")
    AddInt("Unknown")
    AddInt("ScriptId")
    AddInt("ScriptIndex")
    AddInt("Options")
elif f == 3:
    f = AddByte("Function")
    if f == 1:
        AddUnicodeString("UnknownStr")
        # AddShort("Short / X")
    elif f == 3: # Move PC
        AddInt("SomeLocaionId")
    elif f == 4:
        AddUnicodeString("UnknownStr") # BeautyShopDialog
        AddUnicodeString("UnknownStr") # itemcolor
    elif f == 5:
        count = AddInt("count")
        for i in range(count):
            id = AddInt("ItemId")
            AddByte("Unknown") # 1
            AddInt("Unknown") # 1
            DecodeItem(id)
    elif f == 6:
        AddLong("Unknown")
    elif f == 7:
        AddLong("Unknown")
    elif f == 8:
        AddInt("Unknown")
    elif f == 9:
        AddInt("Unknown")
        AddByte("Unknown")
    elif f == 10:
        AddInt("Unknown")
        AddUnicodeString("Unknown")
elif f == 9:
    AddByte("Unknown")
    AddInt("Unknown")
    AddInt("Unknown")
    AddInt("Unknown")
elif f == 10:
    AddInt("Unknown")
    AddShort("Unknown") # some type
    AddInt("Unknown")
    AddByte("Unknown")
    AddInt("Unknown")
    AddByte("Unknown")
    count = AddInt("Unknown")
    for i in range(count):
        t = AddByte("ScriptType")
        if t == 1: # CChatBalloonContent
            DecodeCScriptContent()
        else:
            DecodeCCinematicContent()

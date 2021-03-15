from script_api import *
from common import *

def DecodeListEntry():
    DecodePlayer()

    AddUnicodeString("same char profile url")
    AddLong("???")

    # This is bugged for some equip types
    count = AddByte("EQUIPMENT")
    for j in range(count):
        with Node("Item " + str(j)):
            id = AddInt("Id")
            AddLong("Uid")
            equipType = AddUnicodeString("Type")
            AddInt("??? ^" + str(equipType))
            DecodeItem(id)

    with Node("Badges"):
        count = AddByte("count")
        for j in range(count):
            with Node("Badge " + str(j)):
                AddByte("???")
                id = AddInt("ItemId")
                AddLong("Unknown")
                AddInt("Unknown")
                DecodeItem(id)

    b = AddBool("???")
    if b:
        AddLong("???")
        AddLong("???")
        b = AddBool("flag?")
        if b:
            AddInt("???")
            AddLong("???")
            AddUnicodeString("WStrA")
            AddInt("???")

f = AddByte("Function")
if f == 0:
    charCount = AddByte("Count")
    for i in range(charCount):
        DecodeListEntry()
elif f == 1:
    DecodeListEntry()
elif f == 2: # delete from list
    AddInt("Unknown")
    AddLong("characterId")
elif f == 5: # delete pending
    AddLong("characterId")
    AddInt("Unknown")
    AddLong("DeleteTime")
elif f == 6: # delete cancel
    AddLong("characterId")
    AddInt("Unknown")

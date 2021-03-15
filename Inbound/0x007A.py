from script_api import *
from common import *

AddLong("CharacterId")
b = AddBool("Bool")
if b:
    AddLong("Unknown")
    AddLong("CharacterId")
    AddLong("CurrentTime")

    with Node("Buffer 1", True):
        size = AddInt("BufferSize")
        AddLong("AccountId")
        AddLong("CharacterId")
        AddUnicodeString("Name")
        AddShort("Level")
        AddInt("JobGroupId")
        AddInt("JobId")

        AddInt("Unknown")
        AddInt("Prestige")
        AddByte("Unknown")
        with Node("Stats1"):
            """for i in range(35):
                AddLong("Stat")
            """
            AddField("Stat1", 280)
        with Node("Stats2"):
            """for i in range(35):
                AddLong("Stat")
            """
            AddField("Stat2", 280)
        with Node("Stats3"):
            """for i in range(35):
                AddLong("Stat")
            """
            AddField("Stat3", 280)
        
        with Node("Stats4"):
            for i in range(35):
                AddFloat("Stat")
        
        with Node("UnknownFloatBlock1"):
            for i in range(180):
                prev = AddFloat("UnknownFloat " + str(i) + "|" + (i % 60))
        
        with Node("UnknownFloatBlock2"):
            for i in range(180):
                prev = AddFloat("UnknownFloat " + str(i) + "|" + (i % 60))
        
        AddUnicodeString("ProfileUrl")
        AddUnicodeString("Motto")
        AddUnicodeString("GuildName")
        AddUnicodeString("GuildRank")
        AddUnicodeString("HouseName")
        AddField("Unknown", 12)
        AddInt("TitleId")
        with Node("UnlockedTitles"):
            count = AddInt("Count")
            for i in range(count):
                AddInt("TitleId")
        
        AddInt("TrophyCount")
        AddInt("GearScore")
        AddLong("Timestamp")
        AddLong("Unknown")
        DecodeSkinColor()
        AddShort("Unknown")
        AddUnicodeString("Unknown")
        AddUnicodeString("Unknown")
        AddLong("Unknown")

    with Node("Buffer 2", True):
        size = AddInt("BufferSize")
        count = AddByte("EQUIPMENT")
        for j in range(count):
            with Node("Item " + str(j)):
                id = AddInt("Id")
                AddLong("Uid")
                equipType = AddUnicodeString("Type")
                AddInt("??? ^" + str(equipType))
                DecodeItem(id)
        AddBool("Unknown")
        AddLong("Unknown")
        AddLong("Unknown")
        AddByte("Unknown")

    with Node("Buffer 3", True):
        size = AddInt("BufferSize")
        count = AddByte("count")
        for j in range(count):
            with Node("Badge " + str(j)):
                AddByte("???")
                id = AddInt("ItemId")
                AddLong("Unknown")
                AddInt("Unknown")
                DecodeItem(id)

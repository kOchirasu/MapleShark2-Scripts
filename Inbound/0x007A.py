from script_api import *
from item import *

add_long("CharacterId")
b = add_bool("Bool")
if b:
    add_long("Unknown")
    add_long("CharacterId")
    add_long("CurrentTime")

    with Node("Buffer 1", True):
        size = add_int("BufferSize")
        add_long("AccountId")
        add_long("CharacterId")
        add_unicode_str("Name")
        add_short("Level")
        add_int("JobGroupId")
        add_int("JobId")

        add_int("Unknown")
        add_int("Prestige")
        add_byte("Unknown")
        with Node("Stats1"):
            """for i in range(35):
                add_long("Stat")
            """
            add_field("Stat1", 280)
        with Node("Stats2"):
            """for i in range(35):
                add_long("Stat")
            """
            add_field("Stat2", 280)
        with Node("Stats3"):
            """for i in range(35):
                add_long("Stat")
            """
            add_field("Stat3", 280)
        
        with Node("Stats4"):
            for i in range(35):
                add_float("Stat")
        
        with Node("UnknownFloatBlock1"):
            for i in range(180):
                prev = add_float("UnknownFloat " + str(i) + "|" + (i % 60))
        
        with Node("UnknownFloatBlock2"):
            for i in range(180):
                prev = add_float("UnknownFloat " + str(i) + "|" + (i % 60))
        
        add_unicode_str("ProfileUrl")
        add_unicode_str("Motto")
        add_unicode_str("GuildName")
        add_unicode_str("GuildRank")
        add_unicode_str("HouseName")
        add_field("Unknown", 12)
        add_int("TitleId")
        with Node("UnlockedTitles"):
            count = add_int("Count")
            for i in range(count):
                add_int("TitleId")
        
        add_int("TrophyCount")
        add_int("GearScore")
        add_long("Timestamp")
        add_long("Unknown")
        decode_skin_color()
        add_short("Unknown")
        add_unicode_str("Unknown")
        add_unicode_str("Unknown")
        add_long("Unknown")

    with Node("Buffer 2", True):
        size = add_int("BufferSize")
        count = add_byte("EQUIPMENT")
        for j in range(count):
            with Node("Item " + str(j)):
                id = add_int("Id")
                add_long("Uid")
                equipType = add_unicode_str("Type")
                add_int("??? ^" + str(equipType))
                decode_item(id)
        add_bool("Unknown")
        add_long("Unknown")
        add_long("Unknown")
        add_byte("Unknown")

    with Node("Buffer 3", True):
        size = add_int("BufferSize")
        count = add_byte("count")
        for j in range(count):
            with Node("Badge " + str(j)):
                add_byte("???")
                id = add_int("ItemId")
                add_long("Unknown")
                add_int("Unknown")
                decode_item(id)

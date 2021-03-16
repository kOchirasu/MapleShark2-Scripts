from script_api import *
from common import *

f = add_byte("function")
if f == 6:
    add_long("AccountId")
    add_long("CharacterId")
    add_unicode_str("ProfileUrl")
    add_unicode_str("Name")
    add_short("Level")
    add_int("JobGroupId")
    add_unicode_str("Name")
    add_unicode_str("Message")
    add_byte("Unknown") #1
    add_long("StartTime")
    add_long("EndTime")
    add_long("SomeUid")
    add_int("ItemId")
    add_int("MapId")
    add_int("CoordB guess")
    decode_coordF("RotationGuess")

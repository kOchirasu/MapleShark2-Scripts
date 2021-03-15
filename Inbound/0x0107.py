from script_api import *
from common import *

f = AddByte("function")
if f == 6:
    AddLong("AccountId")
    AddLong("CharacterId")
    AddUnicodeString("ProfileUrl")
    AddUnicodeString("Name")
    AddShort("Level")
    AddInt("JobGroupId")
    AddUnicodeString("Name")
    AddUnicodeString("Message")
    AddByte("Unknown") #1
    AddLong("StartTime")
    AddLong("EndTime")
    AddLong("SomeUid")
    AddInt("ItemId")
    AddInt("MapId")
    AddInt("CoordB guess")
    DecodeCoordF("RotationGuess")

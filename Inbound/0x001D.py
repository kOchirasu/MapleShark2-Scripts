from script_api import *

AddLong("AccountId")
AddLong("CharacterId")
AddUnicodeString("Name")
AddByte("Unknown")
AddUnicodeString("Message")
msgType = AddInt("Type")
AddByte("Unknown")
AddInt("Channel")
if msgType == 3:
    AddUnicodeString("UnknownStr")
elif msgType == 16:
    AddInt("ItemId?")
elif msgType == 20:
    AddLong("CharacterId?")
AddByte("Unknown")

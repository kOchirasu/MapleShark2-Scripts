from script_api import *

# SendServerEnter
AddInt("session id")
AddLong("char id")
AddShort("Unknown")
AddLong("Exp")
AddLong("RestExp")
AddLong("Mesos")
AddLong("Merets")
with Node("Merets 1"):
    AddLong("Merets")
    AddLong("GameMerets")
with Node("Merets 2"):
    AddLong("GameMerets")
    AddLong("EventMerets")
AddLong("ValorToken")
AddLong("Treva")
AddLong("Rue")
AddLong("HaviFruit")
AddLong("Unknown")
AddLong("Unknown")
AddLong("Unknown")
AddLong("Unknown")
AddLong("MesoToken")
AddUnicodeString("Profile URL")
AddByte("Unknown")
AddByte("Unknown")
with Node("Hidden Unlocked Maps?"):
    count = AddShort("Count")
    for i in range(count):
        AddInt("MapId")
with Node("Unlocked Maps"):
    count = AddShort("Count")
    for i in range(count):
        AddInt("MapId")
AddLong("Unknown")
AddUnicodeString("String")
AddUnicodeString("maple news url")
AddUnicodeString("String")
AddUnicodeString("text-nx-cache url")
AddUnicodeString("String")

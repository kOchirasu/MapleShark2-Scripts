from script_api import *

f = AddByte("function")

if f == 1: # request party, or request join
    AddUnicodeString("Name")
elif f == 2: # timeout/decline
    AddUnicodeString("Name")
    AddByte("Type") # 0C = timeout, 09 = decline, 01 = accept
    AddInt("PartyId") # message?
elif f == 3: # leave party
    pass # none
elif f == 4:
    AddLong("Unknown")
elif f == 17: # pass leader
    AddUnicodeString("Name")
elif f == 23:
    AddInt("Unknown")
    AddUnicodeString("Unknown")
    AddLong("Unknown")
elif f == 29:
    pass # none
elif f == 32:
    AddByte("1/2/3/4")
elif f == 33: # SearchForParty
    AddInt("RoomDungeonId")
elif f == 34: # cancel search party
    b = AddByte("1/2/3/4") # sometimes ends here?
    if b != 3:
        AddInt("const 1")
        AddInt("Unknown")
        AddByte("Unknown")
elif f == 45: # vote kick
    AddLong("CharacterId")
elif f == 46: # ready check
    pass # none
elif f == 48: # respond ready check
    AddInt("ReadyCheckConst(34)") # ReadyCheck=34, VoteKick=37
    AddBool("Bool")

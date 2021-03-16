from script_api import *

f = add_byte("function")

if f == 1: # request party, or request join
    add_unicode_str("Name")
elif f == 2: # timeout/decline
    add_unicode_str("Name")
    add_byte("Type") # 0C = timeout, 09 = decline, 01 = accept
    add_int("PartyId") # message?
elif f == 3: # leave party
    pass # none
elif f == 4:
    add_long("Unknown")
elif f == 17: # pass leader
    add_unicode_str("Name")
elif f == 23:
    add_int("Unknown")
    add_unicode_str("Unknown")
    add_long("Unknown")
elif f == 29:
    pass # none
elif f == 32:
    add_byte("1/2/3/4")
elif f == 33: # SearchForParty
    add_int("RoomDungeonId")
elif f == 34: # cancel search party
    b = add_byte("1/2/3/4") # sometimes ends here?
    if b != 3:
        add_int("const 1")
        add_int("Unknown")
        add_byte("Unknown")
elif f == 45: # vote kick
    add_long("CharacterId")
elif f == 46: # ready check
    pass # none
elif f == 48: # respond ready check
    add_int("ReadyCheckConst(34)") # ReadyCheck=34, VoteKick=37
    add_bool("Bool")

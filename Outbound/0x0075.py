from script_api import *

f = AddByte("Function")
if f == 0:
    # Instrument improvise start
    AddLong("ItemUid")
elif f == 1:
    # Play single note
    AddByte("Unknown")
    AddByte("Note") # [24-119] range, +1 for each half-step
    AddShort("Volume")
elif f == 2:
    # Click play score tab
    pass
elif f == 3:
    # Start playing score
    AddLong("InstrumentUid")
    AddLong("ScoreUid")
elif f == 4:
    # Stop playing instrument
    pass
elif f == 8: # Create Music
    AddLong("ItemUid")
    AddField("Unknown", 8) # 24 BF 01 00 10 00 00 00
    AddUnicodeString("SheetName")
    AddString("MusicCode")
elif f == 10: # View Music
    AddLong("ItemUid")
elif f == 11: # queenstown start perform
    pass # none
elif f == 13: # queenstown enter/exit stage
    pass # none
    # Move P:-3600,7200,2125, R:0,0,0
elif f == 14: # queenstown stage fireworks
    pass # none
elif f == 15: # queenstown stage emotes
    AddInt("EmoteId?")

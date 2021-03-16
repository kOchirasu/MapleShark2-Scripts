from script_api import *

f = add_byte("Function")
if f == 0:
    # Instrument improvise start
    add_long("ItemUid")
elif f == 1:
    # Play single note
    add_byte("Unknown")
    add_byte("Note") # [24-119] range, +1 for each half-step
    add_short("Volume")
elif f == 2:
    # Click play score tab
    pass
elif f == 3:
    # Start playing score
    add_long("InstrumentUid")
    add_long("ScoreUid")
elif f == 4:
    # Stop playing instrument
    pass
elif f == 8: # Create Music
    add_long("ItemUid")
    add_field("Unknown", 8) # 24 BF 01 00 10 00 00 00
    add_unicode_str("SheetName")
    add_str("MusicCode")
elif f == 10: # View Music
    add_long("ItemUid")
elif f == 11: # queenstown start perform
    pass # none
elif f == 13: # queenstown enter/exit stage
    pass # none
    # Move P:-3600,7200,2125, R:0,0,0
elif f == 14: # queenstown stage fireworks
    pass # none
elif f == 15: # queenstown stage emotes
    add_int("EmoteId?")

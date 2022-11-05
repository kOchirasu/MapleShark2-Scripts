from script_api import *

f = add_byte("Function")
if f == 0: # Instrument improvise start
    add_long("ItemUid")
elif f == 1: # Play single note (CMidiMessage)
    add_byte("Unknown")
    add_byte("Note") # [24-119] range, +1 for each half-step
    add_short("Volume")
elif f == 2: # Click play score tab
    pass
elif f == 3: # Start playing score
    add_long("InstrumentUid")
    add_long("ScoreUid")
elif f == 4: # Stop playing instrument
    pass
elif f == 5: # start ensemble
    add_long("InstrumentUid")
    add_long("ScoreUid")
elif f == 6: # stop ensemble
    pass
elif f == 8: # Create Music
    add_long("ItemUid")
    add_int("unknown") # 24 BF 01 00
    add_int("unknown") # 10 00 00 00
    add_unicode_str("SheetName")
    add_str("MusicCode")
elif f == 10: # View Music
    add_long("ItemUid")
elif f == 11: # queenstown start perform
    pass
elif f == 12:
    pass # s_music_concert_msg_confirm_unregister
elif f == 13: # queenstown enter/exit stage
    # 802_from_Stage: PortalId=802
    # 803_from_Seats: PortalId=803
    pass
    # Move P:-3600,7200,2125, R:0,0,0
elif f == 14: # queenstown stage fireworks
    pass
elif f == 15: # queenstown stage emotes
    add_int("EmoteId?")

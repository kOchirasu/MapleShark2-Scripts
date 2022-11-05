from script_api import *
from item import *

f = add_byte("Function")
if f == 0: # StartImprovise
    add_int("InstrumentObjectId")
    add_int("PlayerObjectId")
    decode_coordF("InstrumentCoord")
    add_int("GMId")
    add_int("percussionId")
elif f == 1: # play note
    add_int("InstrumentObjectId")
    add_int("PlayerObjectId")
    add_int("MidiNote")
elif f == 2: # StopImprovise
    add_int("InstrumentObjectId")
    add_int("PlayerObjectId")
elif f == 3: # StartScore
    isCustom = add_byte("IsCustom")
    add_int("InstrumentObjectId")
    add_int("PlayerObjectId")
    decode_coordF("InstrumentCoord")
    add_int("InstrumentTick")
    add_int("GMId")
    add_int("percussionId")
    add_bool("Unknown")
    # 36 4B 40 26 18 00 00 00 00 00 00 00 00
    # C4 D6 41 26 18 00 00 00 00 00 00 00 00
    # 76 35 42 26 00 00 00 00 00 00 00 00 00
    # F6 79 70 26 18 00 00 00 00 00 00 00 00
    if isCustom:
        add_str("MusicCode")
    else:
        add_unicode_str("Filename")
elif f == 4: # StopScore
    add_int("InstrumentObjectId")
    add_int("PlayerObjectId")
elif f == 6: # LeaveEnsemble
    pass
elif f == 8: # Create Score response
    add_long("ItemUid")
    decode_item(35100000) # Decode music score item
elif f == 9: # Update remaining uses on score (After start playing)
    add_long("ScoreUid")
    add_int("Remaining uses")
elif f == 10: # View Music
    add_long("ItemUid")
    add_str("MusicCode")
elif f == 14: # Effect related
    add_int("ObjectId")
elif f == 17: # UIWriteMusicDialog, UIPlayInstrumentDialog
    value = add_byte("unknown")
    if value == 8:
        pass
    elif value == 10:
        pass
    elif value == 16:
        pass # s_ban_check_err_all_word

from script_api import *
from common import *

f = add_byte("Function")
if f == 0: # improvise start response
    add_int("InstrumentObjectId")
    add_int("PlayerObjectId")
    decode_coordF("Unknown")
    add_int("Unknown")
    add_int("InstrumentType?")
elif f == 3:
    # BROADCASTED: Started playing instrument
    add_byte("Unknown (1)")
    add_int("InstrumentObjectId")
    add_int("PlayerObjectId")
    decode_coordF("Unknown")
    add_int("Unknown")
    add_int("InstrumentType?")
    add_int("Unknown")
    add_byte("Unknown")
    # 36 4B 40 26 18 00 00 00 00 00 00 00 00
    # C4 D6 41 26 18 00 00 00 00 00 00 00 00
    # 76 35 42 26 00 00 00 00 00 00 00 00 00
    # F6 79 70 26 18 00 00 00 00 00 00 00 00
    add_str("MusicCode")
elif f == 2 or f == 4:
    # BROADCASTED: Stopped/Finished playing instrument
    add_int("InstrumentObjectId")
    add_int("PlayerObjectId")
elif f == 8:
    # Create Score response
    add_long("ItemUid")
    decode_item(35100000) # Decode music score item
elif f == 9:
    # Update remaining uses on score (After start playing)
    add_long("ScoreUid")
    add_int("Remaining uses")
elif f == 10:
    # View Music
    add_long("ItemUid")
    add_str("MusicCode")
elif f == 14:
    add_int("FireworksUnk") # 19986893

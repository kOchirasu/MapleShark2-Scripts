''' LIFTABLE '''
from script_api import *

def decode_liftable(): # CLiftableObject
    add_str("CoordAsHexa")
    add_int("State")  # Removed = 0, Active = 1, Disabled = 2
    add_unicode_str("MaskQuestId")
    add_unicode_str("MaskQuestState")
    add_unicode_str("EffectQuestId")
    add_unicode_str("EffectQuestState")
    add_bool("Unknown") # Always 1?


f = add_byte("Function")
if f == 0:
    count = add_int("count")
    for i in range(count):
        with Node("Liftable " + str(i), True):
            add_str("Entity ID")
            add_byte("Enabled")
            add_int("State") # Removed = 0, Active = 1, Disabled = 2
            add_byte("PickedUp")
            add_unicode_str("MaskQuestId")
            add_unicode_str("MaskQuestState")
            add_unicode_str("EffectQuestId")
            add_unicode_str("EffectQuestState")
            add_bool("Unknown") # Always 1?
elif f == 2:
    add_str("EntityId") # OR CoordAsHexa
    add_byte("Enabled")
    add_int("State") # Removed = 0, Active = 1, Disabled = 2
    add_byte("PickedUp")
elif f == 3:
    decode_liftable()
elif f == 4:
    add_str("CoordAsHexa")

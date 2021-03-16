from script_api import *

f = add_byte("Function")
if f == 3: # Spawn player
    add_int("ObjectId")
    add_long("AccountId")
    add_long("CharacterId")
    add_unicode_str("Name")
    add_unicode_str("Profile Url")
    add_unicode_str("Motto")
    add_byte("Unknown")
    DecordCoordF("Position")
    add_short("Level")
    add_short("JobGroupId")
    add_int("JobId")
    add_int("HomePlotMapId")
    add_int("PlotId")
    add_int("Unknown")
    add_unicode_str("HomeName")
    add_int("GearScore")
    add_short("Unknown")

    # sub_45D8F0
    for i in range(3):
        add_int("Trophies")
if f == 4 or f == 7 or f == 10: # Remove object
    add_int("ObjectId")
elif f == 5:
    add_int("ObjectId")
    flags = add_byte("Flag")
    if (flags & 1) != 0:
        add_byte("C1:Unknown")
    if (flags & 2) != 0:
        add_float("CoordX")
        add_float("CoordY")
        add_float("CoordZ")
    if (flags & 4) != 0:
        add_short("C4:Unknown")
    if (flags & 8) != 0:
        add_short("JobGroupId")
        add_int("JobId")
    if (flags & 16) != 0:
        add_unicode_str("C:16UnknownStr")
    if (flags & 32) != 0:
        add_int("C32:Unknown")
    if (flags & 64) != 0:
        add_short("Animation")
elif f == 6:
    add_int("ObjectId")
    add_int("NpcId")
    add_byte("Unknown")
    add_int("Unknown")
    add_float("CoordX")
    add_float("CoordY")
    add_float("CoordZ")
elif f == 8 or f == 11: # Movement?
    add_int("ObjectId")
    add_byte("Unknown")
    add_float("CoordX")
    add_float("CoordY")
    add_float("CoordZ")
elif f == 9:
    add_int("ObjectId")
    add_int("PetId?")
    add_int("Unknown")
    add_byte("Unknown")
    add_float("CoordX")
    add_float("CoordY")
    add_float("CoordZ")

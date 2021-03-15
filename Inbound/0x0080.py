from script_api import *

f = AddByte("Function")
if f == 3: # Spawn player
    AddInt("ObjectId")
    AddLong("AccountId")
    AddLong("CharacterId")
    AddUnicodeString("Name")
    AddUnicodeString("Profile Url")
    AddUnicodeString("Motto")
    AddByte("Unknown")
    DecordCoordF("Position")
    AddShort("Level")
    AddShort("JobGroupId")
    AddInt("JobId")
    AddInt("HomePlotMapId")
    AddInt("PlotId")
    AddInt("Unknown")
    AddUnicodeString("HomeName")
    AddInt("GearScore")
    AddShort("Unknown")

    # sub_45D8F0
    for i in range(3):
        AddInt("Trophies")
if f == 4 or f == 7 or f == 10: # Remove object
    AddInt("ObjectId")
elif f == 5:
    AddInt("ObjectId")
    flags = AddByte("Flag")
    if (flags & 1) != 0:
        AddByte("C1:Unknown")
    if (flags & 2) != 0:
        AddFloat("CoordX")
        AddFloat("CoordY")
        AddFloat("CoordZ")
    if (flags & 4) != 0:
        AddShort("C4:Unknown")
    if (flags & 8) != 0:
        AddShort("JobGroupId")
        AddInt("JobId")
    if (flags & 16) != 0:
        AddUnicodeString("C:16UnknownStr")
    if (flags & 32) != 0:
        AddInt("C32:Unknown")
    if (flags & 64) != 0:
        AddShort("Animation")
elif f == 6:
    AddInt("ObjectId")
    AddInt("NpcId")
    AddByte("Unknown")
    AddInt("Unknown")
    AddFloat("CoordX")
    AddFloat("CoordY")
    AddFloat("CoordZ")
elif f == 8 or f == 11: # Movement?
    AddInt("ObjectId")
    AddByte("Unknown")
    AddFloat("CoordX")
    AddFloat("CoordY")
    AddFloat("CoordZ")
elif f == 9:
    AddInt("ObjectId")
    AddInt("PetId?")
    AddInt("Unknown")
    AddByte("Unknown")
    AddFloat("CoordX")
    AddFloat("CoordY")
    AddFloat("CoordZ")

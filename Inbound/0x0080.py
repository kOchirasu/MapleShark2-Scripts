from script_api import *
from common import *

f = add_byte("Function")
if f == 3: # Spawn player
    add_int("ObjectId")
    add_long("AccountId")
    add_long("CharacterId")
    add_unicode_str("Name")
    add_unicode_str("Profile Url")
    add_unicode_str("Motto")
    add_byte("CProxyGameObject+3C")
    decode_coordF("Position")
    add_short("Level")
    add_short("JobCode")
    add_int("JobId")
    add_int("HomePlotMapId")
    add_int("PlotId")
    add_int("ApartmentNumber")
    add_unicode_str("HomeName")
    add_int("GearScore")
    add_short("CProxyGameObject+94")

    # sub_45D8F0
    for i in range(3):
        add_int("Trophies")
if f == 4 or f == 7 or f == 10: # Remove object
    add_int("ObjectId")
elif f == 5: # Update
    add_int("ObjectId")
    flags = add_byte("Flag")
    if (flags & 1) != 0:
        add_byte("CProxyGameObject+3C")
    if (flags & 2) != 0:
        decode_coordF("Position")
    if (flags & 4) != 0:
        add_short("level")
    if (flags & 8) != 0:
        add_short("JobCode")
        add_int("JobId")
    if (flags & 16) != 0:
        add_unicode_str("motto")
    if (flags & 32) != 0:
        add_int("gearScore")
    if (flags & 64) != 0:
        add_short("CProxyGameObject+94")
elif f == 6:
    add_int("ObjectId")
    add_int("NpcId")
    add_byte("CProxyGameObject+3C")
    add_int("CProxyGameObject+50") # Counter
    decode_coordF("Position")
elif f == 8 or f == 11: # Movement?
    add_int("ObjectId")
    add_byte("CProxyGameObject+3C")
    decode_coordF("Position")
elif f == 9:
    add_int("ObjectId")
    add_int("PetId?")
    add_int("NpcId")
    add_byte("CProxyGameObject+3C")
    decode_coordF("Position")

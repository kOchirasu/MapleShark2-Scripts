''' LOAD_CUBES '''
from script_api import *
from item import *

f = add_byte("function")

if f == 0: # load cubes
    add_byte("Unknown")
    count = add_int("count")
    for i in range(count):
        with Node("Cube " + str(i)):
            add_int("ByteCoord") # XX YY ZZ 00
            add_long("ItemUid")
            decode_cube_item_info()
            add_int("plotNumber") # cube in plot number on field
            add_int("Unknown")
            add_byte("Unknown")
            add_float("RotationZ")
            add_int("Unknown")
            b = add_bool("Unknown")
            if b: # NoticeCubeInfo
                add_unicode_str("UnknownStr")
                add_byte("Unknown")
elif f == 1: # House Plot Availability
    count = add_int("count")
    for i in range(count):
        with Node("Cube " + str(i)):
            add_int("PlotId")
            add_byte("IsTaken")
elif f == 2: # House Plots
    count = add_int("count")
    for i in range(count):
        with Node("Cube " + str(i)):
            add_int("PlotId")
            add_int("ApartmentNumber")
            add_unicode_str("PlotName")
            add_long("AccountId")
elif f == 3: # House Plot expiration
    count = add_int("count")
    for i in range(count):
        with Node("SaleStateData " + str(i)):
            add_int("PlotId")
            add_int("ApartmentNumber")
            add_byte("State?") # 0, 1=taken, 4=pending
            add_long("ExpirationTime")

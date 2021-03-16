from script_api import *
from common import *

f = add_byte("function")

if f == 0:
    add_byte("Unknown")
    count = add_int("count")
    for i in range(count):
        with Node("Cube " + str(i)):
            add_int("ByteCoord") # XX YY ZZ 00
            add_long("SomeUid")

            with Node("CubeItemInfo"):
                add_int("ItemId")
                add_long("SomeUid")
                add_long("Unknown")
                b = add_bool("IsUGC")
                if b:
                    decode_ugc_data()

            add_int("Unknown")
            add_int("Unknown")
            add_byte("Unknown")
            add_float("Rotation")
            add_int("Unknown")
            b = add_bool("Unknown")
            if b:
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
            add_int("Unknown")
            add_unicode_str("PlotName")
            add_long("AccountId")
elif f == 3: # House Plot related
    count = add_int("count")
    for i in range(count):
        with Node("Cube " + str(i)):
            add_int("PlotId")
            add_int("Unknown")
            add_byte("State?") # 0, 1=taken, 4=pending
            add_long("ExpirationTime?")

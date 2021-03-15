from script_api import *
from common import *

f = AddByte("function")

if f == 0:
    AddByte("Unknown")
    count = AddInt("count")
    for i in range(count):
        with Node("Cube " + str(i)):
            AddInt("ByteCoord") # XX YY ZZ 00
            AddLong("SomeUid")

            with Node("CubeItemInfo"):
                AddInt("ItemId")
                AddLong("SomeUid")
                AddLong("Unknown")
                b = AddBool("IsUGC")
                if b:
                    DecodeUgcData()

            AddInt("Unknown")
            AddInt("Unknown")
            AddByte("Unknown")
            AddFloat("Rotation")
            AddInt("Unknown")
            b = AddBool("Unknown")
            if b:
                AddUnicodeString("UnknownStr")
                AddByte("Unknown")
elif f == 1: # House Plot Availability
    count = AddInt("count")
    for i in range(count):
        with Node("Cube " + str(i)):
            AddInt("PlotId")
            AddByte("IsTaken")
elif f == 2: # House Plots
    count = AddInt("count")
    for i in range(count):
        with Node("Cube " + str(i)):
            AddInt("PlotId")
            AddInt("Unknown")
            AddUnicodeString("PlotName")
            AddLong("AccountId")
elif f == 3: # House Plot related
    count = AddInt("count")
    for i in range(count):
        with Node("Cube " + str(i)):
            AddInt("PlotId")
            AddInt("Unknown")
            AddByte("State?") # 0, 1=taken, 4=pending
            AddLong("ExpirationTime?")

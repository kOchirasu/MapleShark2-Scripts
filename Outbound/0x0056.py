from script_api import *

f = AddByte("function")

if f == 0:
    f2 = AddByte("function2")
    if f2 == 0:
        AddUnicodeString("Log")
        AddUnicodeString("Log")
    elif f2 == 1: # sent every ~5 min by client
        count = AddByte("count") # fps, memory, latency metrics
        for i in range(count):
            with Node("Entry " + str(i), True):
                AddString("Type")
                AddFloat("Average")
                AddFloat("StandardDeviation")
                AddInt("DataPoints")
                AddFloat("Min")
                AddFloat("Max")

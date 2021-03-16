from script_api import *

f = add_byte("function")

if f == 0:
    f2 = add_byte("function2")
    if f2 == 0:
        add_unicode_str("Log")
        add_unicode_str("Log")
    elif f2 == 1: # sent every ~5 min by client
        count = add_byte("count") # fps, memory, latency metrics
        for i in range(count):
            with Node("Entry " + str(i), True):
                add_str("Type")
                add_float("Average")
                add_float("StandardDeviation")
                add_int("DataPoints")
                add_float("Min")
                add_float("Max")

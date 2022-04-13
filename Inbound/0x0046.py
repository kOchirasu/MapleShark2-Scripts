''' ATTRIBUTE_POINT '''
from script_api import *

f = add_byte("function")

if f == 0: # total points
    add_int("TotalAttributePoints")
    count = add_int("count")
    for i in range(count):
        with Node("Attribute " + str(i), True):
            add_int("AttributeType")
            add_int("AllocatedPoints")
elif f == 1: # stat distribution
    add_int("TotalAttributePoints")
    count = add_int("count")
    for i in range(count):
        with Node("Source " + str(i), True):
            add_byte("SourceType")
            add_int("Points")

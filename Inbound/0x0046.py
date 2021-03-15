from script_api import *

f = AddByte("function")

if f == 0:
    AddInt("TotalAttributePoints")
    count = AddInt("count")
    for i in range(count):
        with Node("Attribute " + str(i), True):
            AddInt("AttributeType")
            AddInt("AllocatedPoints")
elif f == 1:
    AddInt("TotalAttributePoints")
    count = AddInt("count")
    for i in range(count):
        with Node("Source " + str(i), True):
            AddByte("SourceType")
            AddInt("Points")

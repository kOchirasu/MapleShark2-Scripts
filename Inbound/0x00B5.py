from script_api import *

count = AddShort("Count")
for i in range(count):
    with Node("Banner " + str(i), True):
        AddInt("Id")
        AddUnicodeString("Name")
        AddUnicodeString("Type")
        AddInt("Zero")
        AddUnicodeString("Url")
        AddInt("Language")
        AddLong("Timestamp")
        AddLong("Unknown")

from script_api import *

def DecodeFunctionCube():
    AddUnicodeString("FunctionCubeName")
    AddInt("State?")
    AddByte("Unknown") # 0/1


f = AddByte("Function")
if f == 2: # load
    count = AddInt("count")
    for i in range(count):
        DecodeFunctionCube()
elif f == 3: # update function cube
    DecodeFunctionCube()
elif f == 5: # manual use function cube
    AddLong("CharacterId")
    AddUnicodeString("FunctionCubeName")
    AddByte("Using (On/Off)")
elif f == 8: # harvest chicken
    AddLong("CharacterId?")
    AddUnicodeString("FunctionCubeName")
    AddLong("TimestampNow")
    AddInt("Amount?")
elif f == 9:
    AddLong("Unknown")
    AddUnicodeString("UnknownStr")
    AddLong("Unknown")
elif f == 10 or f == 11 or f == 13:
    AddLong("Unknown")
    AddUnicodeString("UnknownStr")
elif f == 12:
    AddLong("Unknown")
    AddUnicodeString("UnknownStr")
    AddInt("Unknown")

''' FUNCTION_CUBE '''
from script_api import *

def decode_function_cube():
    add_unicode_str("FunctionCubeName")
    add_int("State?")
    add_byte("Unknown") # 0/1/2
    ''' Don't know what these balues mean but they are mapped
    0 -> 3
    1 -> 4
    2 -> 5
    '''

def decode_nuturing_cube():
    with Node("NurturingCube"):
        add_long("unknown")
        count = add_int("count")
        for i in range(count):
            add_long("unknown")
        count = add_int("count")
        for i in range(count):
            add_long("unknown")


f = add_byte("Function")
if f == 2: # load
    count = add_int("count")
    for i in range(count):
        decode_function_cube()
elif f == 3: # update function cube
    decode_function_cube()
elif f == 5: # manual use function cube, equip related?
    add_long("PlayerId")
    add_unicode_str("FunctionCubeName")
    add_byte("Using (On/Off)")
elif f == 8: # CHomemadeCubeObject
    add_long("CharacterId?")
    add_unicode_str("FunctionCubeName")
    add_long("TimestampNow")
    add_int("Amount?")
elif f == 9: # CHomemadeCubeObject
    add_long("Unknown")
    add_unicode_str("UnknownStr")
    add_long("Unknown")
elif f == 10 or f == 11 or f == 13: # CNurturingCubeObject
    add_long("Unknown")
    add_unicode_str("UnknownStr")
    decode_nuturing_cube()
elif f == 12: # CNurturingCubeObject
    add_long("Unknown")
    add_unicode_str("UnknownStr")
    add_int("Unknown")

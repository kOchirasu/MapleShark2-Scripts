from script_api import *

def decode_function_cube():
    add_unicode_str("FunctionCubeName")
    add_int("State?")
    add_byte("Unknown") # 0/1


f = add_byte("Function")
if f == 2: # load
    count = add_int("count")
    for i in range(count):
        decode_function_cube()
elif f == 3: # update function cube
    decode_function_cube()
elif f == 5: # manual use function cube
    add_long("CharacterId")
    add_unicode_str("FunctionCubeName")
    add_byte("Using (On/Off)")
elif f == 8: # harvest chicken
    add_long("CharacterId?")
    add_unicode_str("FunctionCubeName")
    add_long("TimestampNow")
    add_int("Amount?")
elif f == 9:
    add_long("Unknown")
    add_unicode_str("UnknownStr")
    add_long("Unknown")
elif f == 10 or f == 11 or f == 13:
    add_long("Unknown")
    add_unicode_str("UnknownStr")
elif f == 12:
    add_long("Unknown")
    add_unicode_str("UnknownStr")
    add_int("Unknown")

''' FIELD_PROPERTY '''
from script_api import *

def decode_field_property_info(t: int):
    if t == 1: # Gravity
        add_float("Unknown")
    elif t == 2: # Concert (queenstown)
        add_long("CharacterId")
        add_int("Unknown") # 2252735185
    elif t == 3: # HideMyPC
        add_unicode_str("Unknown")
        add_unicode_str("Unknown")
    elif t == 4: # LockMyPC
        add_unicode_str("Unknown")
        add_unicode_str("Unknown")
    elif t == 5: # UserTagSymbol
        add_unicode_str("Unknown")
        add_unicode_str("Unknown")
    elif t == 6: # SightRange
        add_float("Unknown")
        add_float("Unknown")
        add_float("Unknown")
        add_float("Unknown")
        add_bool("Unknown")
        add_byte("Unknown")
        add_bool("Unknown")
    elif t == 7: # Weather
        add_byte("Unknown")
    elif t == 8: # AmbientLight
        with Node("Color"):
            add_byte("Red")
            add_byte("Green")
            add_byte("Blue")
    elif t == 9: # DirectionalLight
        with Node("DiffuseColor"):
            add_byte("Red")
            add_byte("Green")
            add_byte("Blue")
        with Node("SpecularColor"):
            add_byte("Red")
            add_byte("Green")
            add_byte("Blue")
    elif t == 10: # Enables "Local Camera"
        add_bool("IsEnabled?")
    elif t == 11: # Enables "FreeCamera/Take a Screenshot"
        add_bool("IsEnabled?")


f = add_byte("Function")
if f == 0:
    count = add_int("count")
    for i in range(count):
        t = add_byte("type")
        decode_field_property_info(t)
elif f == 1:
    t = add_byte("type")
    decode_field_property_info(t)
elif f == 2:
    add_byte("type")

from script_api import *

def DecodeFieldPropertyInfo(t):
    if t == 1: # Gravity
        AddFloat("Unknown")
    elif t == 2: # Concert (queenstown)
        AddLong("CharacterId")
        AddInt("Unknown") # 2252735185
    elif t == 3: # HideMyPC
        AddUnicodeString("Unknown")
        AddUnicodeString("Unknown")
    elif t == 4: # LockMyPC
        AddUnicodeString("Unknown")
        AddUnicodeString("Unknown")
    elif t == 5: # UserTagSymbol
        AddUnicodeString("Unknown")
        AddUnicodeString("Unknown")
    elif t == 6: # SightRange
        AddFloat("Unknown")
        AddFloat("Unknown")
        AddFloat("Unknown")
        AddFloat("Unknown")
        AddBool("Unknown")
        AddByte("Unknown")
        AddBool("Unknown")
    elif t == 7: # Weather
        AddByte("Unknown")
    elif t == 8: # AmbientLight
        with Node("Node"):
            AddByte("Unknown")
            AddByte("Unknown")
            AddByte("Unknown")
    elif t == 9: # DirectionalLight
        with Node("Node"):
            AddByte("Unknown")
            AddByte("Unknown")
            AddByte("Unknown")
        with Node("Node"):
            AddByte("Unknown")
            AddByte("Unknown")
            AddByte("Unknown")
    elif t == 10: # Enables "Local Camera"
        AddBool("IsEnabled?")
    elif t == 11: # Enables "FreeCamera/Take a Screenshot"
        AddBool("IsEnabled?")


f = AddByte("Function")
if f == 0:
    count = AddInt("count")
    for i in range(count):
        t = AddByte("type")
        DecodeFieldPropertyInfo(t)
elif f == 1:
    t = AddByte("type")
    DecodeFieldPropertyInfo(t)
elif f == 2:
    AddByte("Unknown")

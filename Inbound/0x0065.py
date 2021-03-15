from script_api import *
from common import *

f = AddByte("function")

if f == 4:
    AddString("EntityId")
    AddByte("Unknown") # 0 <- visible?
    AddByte("Unknown") # 1
elif f == 5: # after interacting, despawn?
    AddString("EntityId")
    AddByte("Unknown") # 6 (index?)
    # ... (00 00 01 00 00 00)
elif f == 6:
    AddInt("InteractId")
    AddByte("Unknown")
elif f == 7:
    AddByte("Unknown")
elif f == 8:
    count = AddInt("count")
    for i in range(count):
        with Node("Interact " + str(i)):
            AddString("EntityId")
            AddByte("Unknown")
            b = AddByte("Unknown")
            if b == 6:
                AddInt("Unknown")
elif f == 9:
    AddString("Name") # EventCreate_982795
    AddByte("Unknown")
    AddByte("Unknown")
    AddInt("InteractObjectId")
    DecodeCoordF("Position")
    DecodeCoordF("Rotation")
    AddUnicodeString("InteractXmlType") # MS2InteractActor/MS2InteractMesh
    AddUnicodeString("UnknownStr") # interaction_chestA_02
    AddUnicodeString("UnknownStr") # Opened_A/Interaction_advertisement_A01
    AddUnicodeString("UnknownStr") # Idle_A/Interaction_advertisement_A01
    AddFloat("Unknown")
    AddBool("Unknown")
    # Some other conditional cases
    AddLong("Unknown")
    AddUnicodeString("OwnerIgn")
elif f == 10:
    AddString("Unknown")
    AddUnicodeString("Unknown")
elif f == 13: # respawn? | gold chest remove #2
    AddByte("Unknown") # 0 <- visible?
    AddString("EntityId")
    AddByte("Unknown") # index? (6, 1)
    # ...?
elif f == 14:
    AddShort("Unknown")
    AddInt("Unknown")
    AddInt("Unknown")
    AddUnicodeString("Unknown")
elif f == 15:
    AddInt("Unknown")
    AddInt("Unknown")

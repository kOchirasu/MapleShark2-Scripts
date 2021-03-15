from script_api import *

def DecodeType1():
    AddInt("CubeCount")
    AddInt("Unknown")
    b = AddBool("HasUgcDetails")
    if b:
        accountId = AddLong("AccountId?")
        AddUnicodeString("HomeName")
        AddUnicodeString("HomeMessage")
        AddByte("Unknown")
        AddInt("WeelkyArchitectScore")
        AddInt("TotalArchitectScore")
        AddInt("PlotId")
        AddInt("PlotMapId")
        AddByte("Unknown")
        AddByte("AreaDimension")
        AddByte("HeightDimension")
        with Node("InteriorSettings", True):
            AddByte("Background")
            AddByte("Lighting")
            AddByte("Camera")
        
        with Node("HomePermissions", True):
            # 0 - Jumping
            # 1 - Wall Climbing
            # 2 - Skill Use
            # 3 - Music Performance
            # 4 - Potion Use
            # 5 - Ground Mounts
            # 6 - Air Mounts
            # 7
            # 8
            count = AddByte("Count")
            for i in range(count):
                StartNode("Permission " + str(i))
                n = AddBool("IsConfigured")
                if n:
                    # 0 - Allow None
                    # 1 - Allow Me
                    # 2 - Allow My Party
                    AddByte("Value")
                EndNode(n)
        
        with Node("DesignNode", True):
            if accountId != 0: # Another unknown condition
                count = AddByte("Count")
                for i in range(count):
                    with ("SavedDesign " + str(i)): # UGCMapDesignInfo
                        AddInt("SaveSlot")
                        AddUnicodeString("Name")
                        AddLong("SaveTime")

                count = AddByte("Count")
                for i in range(count):
                    with Node("UGCMapBlueprintInfo " + str(i)):
                        AddInt("Unknown")
                        AddUnicodeString("UnknownStr")
                        AddLong("Unknown")
        

DecodeType1()
from script_api import *

def decode_type1():
    add_int("CubeCount")
    add_int("Unknown")
    b = add_bool("HasUgcDetails")
    if b:
        accountId = add_long("AccountId?")
        add_unicode_str("HomeName")
        add_unicode_str("HomeMessage")
        add_byte("Unknown")
        add_int("WeelkyArchitectScore")
        add_int("TotalArchitectScore")
        add_int("PlotId")
        add_int("PlotMapId")
        add_byte("Unknown")
        add_byte("AreaDimension")
        add_byte("HeightDimension")
        with Node("InteriorSettings", True):
            add_byte("Background")
            add_byte("Lighting")
            add_byte("Camera")
        
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
            count = add_byte("Count")
            for i in range(count):
                start_node("Permission " + str(i))
                n = add_bool("IsConfigured")
                if n:
                    # 0 - Allow None
                    # 1 - Allow Me
                    # 2 - Allow My Party
                    add_byte("Value")
                end_node(n)
        
        with Node("DesignNode", True):
            if accountId != 0: # Another unknown condition
                count = add_byte("Count")
                for i in range(count):
                    with ("SavedDesign " + str(i)): # UGCMapDesignInfo
                        add_int("SaveSlot")
                        add_unicode_str("Name")
                        add_long("SaveTime")

                count = add_byte("Count")
                for i in range(count):
                    with Node("UGCMapBlueprintInfo " + str(i)):
                        add_int("Unknown")
                        add_unicode_str("UnknownStr")
                        add_long("Unknown")
        

decode_type1()
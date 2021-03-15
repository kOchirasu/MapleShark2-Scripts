from script_api import *
from common import *

count = AddShort("Count")
for i in range(count):
    with Node("NpcControl " + str(i), True):
        size = AddShort("BufferSize")
        oid = AddInt("ObjectId")
        AddByte("Flags") # bit-1, bit-2
        DecodeCoordS("Position")
        AddShort("Rotation / 10")
        DecodeCoordS("Speed")
        AddShort("Short / 100") # 100
        # Dummy (not friendly and class >= 3)
        if oid == 5338377 or oid == 5338398 or oid == 10000003 or oid == 10000002:
            AddInt("TargetObject")
        n = AddByte("Flag")
        a = AddShort("Animation") #  -2 = Jump_A, -3 = Jump_B
        AddShort("Counter (per action)")

        if a == -2 or a == -3:
            with Node("JumpInfo", True):
                b = AddBool("Flag?")
                if b:
                    DecodeCoordF("StartPosition")
                    DecodeCoordF("EndPosition")
                    AddFloat("Duration (s)")
                    AddFloat("Height")
                else:
                    DecodeCoordF("EndPosition") # relative
                    # duration = 1?
                    # height = 0.45

        """
        case 1: // Idle
        case 2: // Walk
        case 6: // Jump
        case 12: // Dead
        case 13: // StateHitData
        case 16: // Skill
        case 17: // StateSpawnData
        case 18: // Stun
        case 22: // Talk
        case 23: // Regen
        case 35: // Puppet
        case 56: // SummonPortal
        """
        if n == 1 or n == 2 or n == 6 or n == 12 or n == 13:
            AddFloat("StateHitUnknown")
            AddFloat("StateHitUnknown")
            AddFloat("StateHitUnknown")
            AddByte("StateHitUnknown")
        elif n == 16 or n == 17:
            AddInt("StateSpawnUnknown")
        elif n == 18 or n == 22 or n == 23 or n == 35 or n == 56:
            pass
    EndNode(True)

from script_api import *
from common import *

count = add_short("Count")
for i in range(count):
    with Node("NpcControl " + str(i), True):
        size = add_short("BufferSize")
        oid = add_int("ObjectId")
        add_byte("Flags") # bit-1, bit-2
        decode_coordS("Position")
        add_short("Rotation / 10")
        decode_coordS("Speed")
        add_short("Short / 100") # 100
        # Dummy (not friendly and class >= 3)
        if oid == 5338377 or oid == 5338398 or oid == 10000003 or oid == 10000002:
            add_int("TargetObject")
        n = add_byte("Flag")
        a = add_short("Animation") #  -2 = Jump_A, -3 = Jump_B
        add_short("Counter (per action)")

        if a == -2 or a == -3:
            with Node("JumpInfo", True):
                b = add_bool("Flag?")
                if b:
                    decode_coordF("StartPosition")
                    decode_coordF("EndPosition")
                    add_float("Duration (s)")
                    add_float("Height")
                else:
                    decode_coordF("EndPosition") # relative
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
            add_float("StateHitUnknown")
            add_float("StateHitUnknown")
            add_float("StateHitUnknown")
            add_byte("StateHitUnknown")
        elif n == 16 or n == 17:
            add_int("StateSpawnUnknown")
        elif n == 18 or n == 22 or n == 23 or n == 35 or n == 56:
            pass
    end_node(True)

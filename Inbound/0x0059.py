''' NPC_CONTROL '''
from script_api import *
from common import *

def decode_npc_control_buffer():
    size = add_short("BufferSize")
    # Buffer
    objectId = add_int("ObjectId")
    add_byte("Flags") # bit-1, bit-2
    decode_coordS("Position")
    add_short("Rotation / 10")
    decode_coordS("Speed")
    add_short("Short / 100") # 100
    # if (not friendly and class >= 3)
    '''
    add_int("TargetObject")
    '''
    state = add_byte("state")
    seqId = add_short("SequenceId") # from anikeytext.xml
    add_short("Counter (per action)")

    if seqId == -2 or seqId == -3: # -2 = Jump_A, -3 = Jump_B
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
    # special logic handling for: prefix("Run_")
    # special logic for: knockback_distance == 0 && state != 17|gosSpawn

    if state == 13: # gosHit
        add_float("StateHitUnknown")
        add_float("StateHitUnknown")
        add_float("StateHitUnknown")
        add_byte("StateHitUnknown")
    elif state == 17: # gosSpawn
        add_int("StateSpawnUnknown")
    elif state == 18: # gosStun OR knockback_distance != 0
        pass
    elif state == 22: # gosTalk
        '''
        if pc.subState != 73|StateTalk_Idle or not fieldObject:
            if pc.subState == 72|StateTalk_Loop and fieldObject:
                pass # ???
        else:
            pass # QuestManager
        '''
        pass
    elif state == 56: # gosSummonPortal
        pass # QuestManager


count = add_short("Count")
for i in range(count):
    with Node("NpcControl " + str(i), True):
        decode_npc_control_buffer()

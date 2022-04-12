''' INTERACT_OBJECT '''
from script_api import *
from common import *

def decode_interact_object(type):
    if type == 1: # CInteractMeshObject
        pass # nullsub
    elif type == 2: # CInteractTelescopeObject
        # s_cutscene_telescope_keycap, s_cutscene_telescope_keydesc
        pass # sub_B2F510
    elif type == 3: # CInteractUIObject
        pass # sub_B2E280
    elif type == 4: # CInteractWebObject
        pass # nullsub
    elif type == 5: # CInteractDisplayImage
        pass # nullsub
    elif type == 6: # CInteractGatheringObject
        add_short("unknown")
        add_int("unknown")
    elif type == 7: # CInteractGuildPosterObject
        pass # nullsub
    elif type == 8: # CInteractBillBoardObject
        pass # nullsub
    elif type == 9: # CInteractWatchTowerObject
        pass # nullsub


f = add_byte("function")
if f == 4:
    add_str("EntityId")
    add_bool("CInteract[5]") # 0 <- visible?
    add_byte("InteractType")
elif f == 5: # after interacting, despawn?
    add_str("EntityId")
    t = add_byte("InteractType")
    decode_interact_object(t)
elif f == 6:
    add_int("InteractId")
    add_bool("CInteract[5]") # 0 <- visible?
elif f == 7:
    add_bool("CInteract[5]") # 0 <- visible?
elif f == 8:
    count = add_int("count")
    for i in range(count):
        with Node("Interact " + str(i)):
            add_str("EntityId")
            add_bool("CInteract[5]") # 0 <- visible?
            b = add_byte("InteractType")
            if b == 6: # CInteractGatheringObject
                add_int("Unknown")
elif f == 9:
    add_str("Name") # EventCreate_982795
    add_bool("CInteract[5]") # 0 <- visible?
    add_byte("InteractType") # see decode_interact_object
    add_int("InteractObjectId") # Gamebryo:resource_id:188
    decode_coordF("Position") # Gamebryo:resource_id:82
    decode_coordF("Rotation") # Gamebryo:resource_id:157
    add_unicode_str("InteractXmlType") # MS2InteractActor,MS2InteractMesh
    add_unicode_str("Gamebryo:resource_id:45") # interaction_chestA_02 <- urn:gamebryo-animation:
    add_unicode_str("Gamebryo:resource_id:200") # Opened_A/Interaction_advertisement_A01
    add_unicode_str("Gamebryo:resource_id:74") # Idle_A/Interaction_advertisement_A01
    add_float("Gamebryo:resource_id:45")
    add_bool("Gamebryo:resource_id:243")
    # Some other conditional cases
    # if (CInteractBillBoardObject)
    '''
    add_long("Unknown")
    add_unicode_str("OwnerIgn")
    '''
elif f == 10:
    add_str("Unknown")
    add_unicode_str("Unknown") # effect
elif f == 13: # respawn? | gold chest remove #2
    message = add_byte("message")
    add_str("EntityId")
    add_byte("InteractType") # see decode_interact_object
    '''
    if message == 0:
        pass # s_interact_find_new_telescope
    elif message == 1:
        pass # s_interact_result_unknown
    elif message == 2:
        pass # s_interact_result_quest
    elif message == 3:
        pass # s_interact_result_party
    elif message == 4:
        pass # s_tutorial_dialog_limit
    elif message == 5:
        pass # s_interact_result_privilege
    elif message == 7:
        pass # s_interact_result_auth
    elif message == 12:
        pass # none
    elif type == 13:
        message # s_interact_result_mastery
    '''
elif f == 14:
    n = add_short("Unknown")
    add_int("Unknown")
    add_int("Unknown")
    add_unicode_str("Unknown")
elif f == 15:
    add_int("ObjectId")
    add_int("ItemId")

''' FIELD_ADD_PET '''
from script_api import *
from common import *
from stats import *

add_int("ObjectId")
add_int("PetSkinId")
add_int("PetNpcId")
decode_coordF("Position") # client adds 4.0f to |z|
decode_coordF("Rotation")
add_float("Unknown") # 1.0f, scale?
add_int("OwnerObjectId")
decode_npc_stats()
add_long("PetItemUid")
add_byte("CNpc+18F0")
add_short("Level")
add_short("PetTaming") # calls lua calc_PetTamingRank
add_int("CNpc+1928")
add_unicode_str("Name")

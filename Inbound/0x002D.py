''' FIELD_PICKUP_ITEM '''
from script_api import *

b = add_bool("picked up")
add_int("ObjectId")
if b:
    add_int("ObjectId") # object id of the player who picked up

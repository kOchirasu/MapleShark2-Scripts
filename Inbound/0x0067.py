''' STATE_FALL_DAMAGE '''
from script_api import *

add_int("ObjectId")
add_int("damage")

'''
function calc_fallDamage(mhpV, fallDistance)
	local rst_damage = (mhpV * 7 * ((fallDistance - 750) / 150)) / 100
	return math.max(rst_damage, 0)
end
'''

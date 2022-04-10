''' JOB '''
from script_api import *
from common import *

# Request 0x0025 08 (SendJob)
# Response This packet
add_int("ObjectId")
f = add_byte("function") # 2 for awakening?
if f == 0: # unknown
    decode_skill_tree()
    # UIRewardNotify
elif f == 1 or f == 2:
    decode_skill_tree()
    # UIRewardNotify
    if f == 2:
        pass # UIChangeJobEffect
elif f == 7:
    decode_skill_tree()
    # UIRewardNotify
elif f == 9 or f == 10 or f == 11:
    ''' These are all handled the same by the client?
    9 = Update
    10 = Reset
    11 = Auto-Distribute
    '''
    decode_skill_tree()
    # UIGameMenuDialog
elif f == 8: # load
    decode_skill_tree()
else: # error, this is function 3 basically
    message = add_byte("message")
    '''
    if message == 2:
        pass # s_err_job_bad_job
    elif message == 3 or message == 4:
        pass # s_err_job_not_complete_quest
    elif message == 5:
        pass # s_err_job_privilege
    elif message == 8:
        pass # s_err_job_not_enough_meso
    elif message == 10:
        pass # s_err_job_not_enough_level
    elif message == 11:
        pass # s_err_job_no_home
    elif message == 12:
        pass # s_err_job_no_penalty
    elif message == 14:
        pass # s_err_job_guild
    elif message == 15:
        pass # s_err_job_dayofweek
    elif message == 18:
        pass # s_err_job_inventory_full
    else:
        pass # s_err_job_unknown
    '''
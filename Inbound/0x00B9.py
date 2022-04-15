''' HOME_COMMAND '''
from script_api import *

f = add_byte("function")

if f == 0: # load home
    add_long("AccountId")
    add_long("LastTimePlayerNominatedHome")
elif f == 1: # update architect score
    add_int("HomeOwnerObjectId")
    add_long("TimestampNow")
    add_int("WeeklyArchitectScore")
    add_int("TotalArchitectScore")
else:
    add_int("ObjectId")
    add_long("TimestampNow")
    add_int("WeeklyArchitectScore")
    add_int("TotalArchitectScore")

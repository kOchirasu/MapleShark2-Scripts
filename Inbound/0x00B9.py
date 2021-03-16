from script_api import *

f = add_byte("function")

if f == 0:
    add_long("AccountId?")
    add_long("Timestamp 2 days ago...?")
elif f == 1: # sent after thumbs up
    add_int("HomeOwnerObjectId")
    add_long("TimestampNow")
    add_int("WeeklyArchitectScore")
    add_int("TotalArchitectScore")

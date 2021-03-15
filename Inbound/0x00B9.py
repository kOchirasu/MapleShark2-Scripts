from script_api import *

f = AddByte("function")

if f == 0:
    AddLong("AccountId?")
    AddLong("Timestamp 2 days ago...?")
elif f == 1: # sent after thumbs up
    AddInt("HomeOwnerObjectId")
    AddLong("TimestampNow")
    AddInt("WeeklyArchitectScore")
    AddInt("TotalArchitectScore")

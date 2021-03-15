from script_api import *

def AddAchievementDetails():
    AddByte("Type")
    AddInt("StartGrade")
    AddInt("CurrentGrade")
    AddInt("EndGrade")
    AddByte("Unknown")
    AddLong("TrackerTotalCount")
    count2 = AddInt("Count")
    for j in range(count2):
        AddInt("Grade " + (j + 1))
        AddLong("DateAchieved")

f = AddByte("Function")
if f == 1: # Load
    count = AddInt("Count")
    for i in range(count):
        with Node("Achievment " + str(i)):
            AddInt("Id")
            AddInt("ss")
            AddAchievementDetails()
elif f == 2: # Update?
    AddInt("Id")
    AddAchievementDetails()

''' ACHIEVE '''
from script_api import *

def decode_achieve_details():
    add_byte("Type")
    add_int("StartGrade")
    add_int("CurrentGrade")
    add_int("EndGrade")
    add_byte("Unknown")
    add_long("TrackerTotalCount")
    count2 = add_int("Count")
    for j in range(count2):
        add_int("Grade " + (j + 1))
        add_long("DateAchieved")

f = add_byte("Function")
if f == 1: # Load
    count = add_int("Count")
    for i in range(count):
        with Node("Achievment " + str(i)):
            add_int("Id")
            add_int("unknown")
            decode_achieve_details()
elif f == 2: # Update?
    add_int("Id")
    decode_achieve_details()

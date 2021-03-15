from script_api import *

# Request pickup for meso objects
count = AddByte("Count")
for i in range(count):
    AddInt("ObjectId")

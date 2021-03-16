from script_api import *

# Request pickup for meso objects
count = add_byte("Count")
for i in range(count):
    add_int("ObjectId")

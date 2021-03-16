from script_api import *

f = add_byte("function")

if f == 6:
    count = add_int("count")
    for i in range(count):
        add_int("Id")
        add_long("Timestamp")

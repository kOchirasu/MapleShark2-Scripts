from script_api import *

count = add_short("Count")
for i in range(count):
    with Node("Banner " + str(i), True):
        add_int("Id")
        add_unicode_str("Name")
        add_unicode_str("Type")
        add_int("Zero")
        add_unicode_str("Url")
        add_int("Language")
        add_long("Timestamp")
        add_long("Unknown")

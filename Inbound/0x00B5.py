''' BANNER_LIST '''
from script_api import *

count = add_short("Count")
for i in range(count):
    with Node("AdBannerData " + str(i), True):
        add_int("Id")
        add_unicode_str("Name")
        add_unicode_str("Type")
        add_unicode_str("unknown")
        add_unicode_str("unknown")
        add_unicode_str("Url")
        add_int("Language")
        add_long("Timestamp")
        add_long("Unknown")

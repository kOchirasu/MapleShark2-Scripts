from script_api import *


f = add_byte("Function")
if f == 17:
    add_unicode_str("Endpoint 1")
    add_unicode_str("Endpoint 2")
    add_unicode_str("Locale")
    add_byte("const")
elif f == 22:
    add_int("const")

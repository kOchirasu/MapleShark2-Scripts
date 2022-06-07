''' WARDROBE '''
from script_api import *

f = add_byte("function")
if f == 0:
  add_int("index")
  add_int("isOutfit")
elif f == 1:
  add_int("index")
  add_int("isOutfit")
elif f == 2:
  add_int("index")
elif f == 4:
  add_int("index")
  add_int("key")
elif f == 6:
  add_int("index")
  add_unicode_str("name")
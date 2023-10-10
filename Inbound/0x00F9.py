''' EVENT_REWARD '''
from script_api import *

f = add_byte("Function")
if f == 0 or f == 1: # UIStampEventDialog
    count = add_int("count")
    for i in range(count):
      add_int("itemId")
      add_short("rarity")
elif f == 3 or f == 4: # UITimeRunEventDialog
    add_int("itemId")
    add_short("rarity")
elif f == 7: # UIGalleryEventDialog, openCard
    add_byte("unknown")
elif f == 8: # UIGalleryEventDialog, quest
    add_byte("questState")
elif f == 9: # UIGalleryEventDialog, reward
    count = add_int("count")
    for i in range(count):
      add_int("itemId")
      add_short("rarity")
elif f == 12 or f == 13: # UISnowmanEventDialog
    count = add_int("count")
    for i in range(count):
      add_int("itemId")
      add_short("rarity")
elif f == 23: # Unknown
    count = add_int("count")
    for i in range(count):
      add_int("itemId")
      add_short("rarity")

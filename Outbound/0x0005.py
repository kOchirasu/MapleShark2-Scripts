from script_api import *

""" GameToGame
Client | Server
       < 0x04 |
  0x05 >      | 01 [8B 79 08 FE 3D 95 3D 26] [A6 1A EB 26 56 95 3B 26] 01 00 00 00 09 72 01 00 [StrW (Hwid?)] 01 00 00 00 [StrA (Key)] 84 1F 00 00
       < 0x05 | 00 01 00 00 00 [StrA (Key)] 84 1F 00 00
       < 0x07 | 09 72 01 00
       < 0x08 | 17 72 01 00 88 2F 01 00
  0x07 >      | 88 2F 01 00
  0x08 >      | 8F 2F 01 00
       < 0x05 | 02 01 00 00 00
       < 0xE8 | BypassKey
"""

f = add_byte("function")

if f == 1:
    add_long("AccountId")
    add_long("CharacterId")
    add_int("Unknown") # count?
    add_int("Unknown")
    add_unicode_str("Unknown") # 74-C6-3B-ED-0A-A6-7D-D2-ED-D8-00-00-00-00-E3-23
    add_int("Unknown") # count?
    add_str("SomeKey") # CjhWVm0HAAB2wucC3975500370134093852
    add_int("Unknown")

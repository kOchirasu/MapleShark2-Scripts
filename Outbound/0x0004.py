from script_api import *

# Example:
# < 01 00 AB 8C 13 00 00 00 01 00 0C 00 00 00 B4 2C 1C B5 22 C6 A7 8C 0D 00 00 00 02
# > 01 00 0C 00 00 00 2F 00 02 00
# < 04 00
# > 04 00 [B2 79 72 04 3E 95 3C 26] [90 CB 99 00] [2B 86 44 19] 74 C6 3B ED 0A A6 7D D2 ED D8 00 00 00 00 E3 23
add_long("AccountId")
add_int("TokenA")
add_int("TokenB")
add_field("MachineId", 16) # 16byte buffer (machineid?)

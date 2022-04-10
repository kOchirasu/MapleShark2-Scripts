from script_api import *
from common import *

f = add_byte("function")
if f == 0: # start hongbao
    add_int("ItemId")
    add_int("HongBaoUid")
    add_int("RewardItemId")
    add_int("RewardAmount")
    add_int("MaxRewardedPlayers")
    add_unicode_str("HostCharacterId")
elif f == 2: # hongbao gift notice
    active = add_byte("HongBaoIsActive") # bool
    if active == 1:
        add_int("HongBaoItemId")
        add_int("RewardItemId")
        add_int("DividedRewardAmount")
        add_unicode_str("HongBaoHostCharacterName")
        add_unicode_str("RewardedCharacterName")
elif f == 3: # start player hosted minigame
    add_unicode_str("HostCharacterName")
    add_int("MiniGameMapId")
elif f == 4: # minigame reward notice
    add_int("MiniGameMapId")
    add_int("PlayerCount")
elif f == 5: # minigame reward receive
    add_int("MiniGameMapId")
    add_int("PlayerCount")
elif f == 6: # ad balloon window
    add_long("AccountId")
    add_long("CharacterId")
    add_unicode_str("ProfileUrl")
    add_unicode_str("Name")
    add_short("Level")
    add_int("JobGroupId")
    add_unicode_str("Name")
    add_unicode_str("Message")
    add_byte("PublicHome") #bool if house is public
    add_long("StartTime")
    add_long("EndTime")
    add_long("SomeUid")
    add_int("ItemId")
    add_int("MapId")
    add_int("CoordB guess")
    decode_coordF("RotationGuess")
elif f == 7: # place ad balloon
    add_int("Unknown")

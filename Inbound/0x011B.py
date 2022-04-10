from script_api import *

f = add_byte("Function")
if f == 0: # join solo queue
    pass
elif f == 1: # withdraw solo queue
    pass
elif f == 2: # match found
    add_long("MatchId")
    add_byte("PromptDuration") # if == 1, 15 second window. if == 0, 5 second
elif f == 17: # results
    add_int("Unknown")
    add_int("Unknown")
    add_int("PreviousPointCount")
    add_int("CurrentPointcount")
    add_int("TotalPlayersInMatch")
    add_int("RankInMatch")
    add_int("Unknown")
    add_int("Unknown")
    add_int("RoyaleExp")
    add_int("Unknown")
    add_int("RoyaleLevel")
    add_int("Unknown")
    add_int("PlayerExp") # normal exp
    add_int("PresitgeExp")
    add_int("TimeSurvived")
    add_int("KillCount")
    add_int("Unknown")
    add_int("Unknown")
    add_int("Unknown")
    add_int("Unknown")
    items = add_byte("ItemRewardsCount")
    for i in range(items):
        add_int("ItemId")
        add_short("ItemRarity")
        add_int("ItemAmount")
        add_byte("Unknown")
        add_byte("Unknown")
        add_byte("Unknown")
elif f == 20: # last standing notice
    add_byte("Unknown")
    playerCount = add_int("PlayerCount")
    for i in range(playerCount):
        add_long("CharacterId")
elif f == 22:
    add_int("Unknown")
    add_int("Unknown")
    add_long("Unknown")
    add_unicode_str("UnknownStr")
    add_int("Unknown")
    add_int("Unknown")
    add_int("Unknown")
    add_int("Unknown")
    add_int("Unknown")
    add_int("Unknown")
    add_int("Unknown")
elif f == 23: # update survival stats
    add_long("StatsId")
    add_int("Unknown")
    add_byte("GoldPassActive") # bool
    add_long("SurvivalExp")
    add_int("SurvivalLevel")
    add_int("SilverLevelClaimedRewards") # last level of claimed rewards
    add_int("GoldLevelClaimedRewards") # last level of claimed rewards
    add_long("ExpGained")
elif f == 24: # new season notice
    pass
elif f == 26: # update kills
    add_int("KillCount")
elif f == 27: # survival match stats
    add_int("PlayersRemaining")
    add_int("TotalPlayers")
    add_byte("Unknown")
elif f == 29: # poisoned notice
    pass
elif f == 30: # update survival medals
    count = add_byte("TotalMedalCount")
    for i in range(count):
        add_int("EquippedMedalEffectId")
        count2 = add_int("MedalSlotCount")
        for j in range(count2):
            add_int("MedalEffectId")
            add_long("MedalExpirationTime")
elif f == 35: # claim rewards
    add_int("SilverStartLevel") # start level of rewards to claim
    add_int("SilverEndLevel") # end level of rewards to claim
    add_int("GoldStartLevel")
    add_int("GoldEndLevel")

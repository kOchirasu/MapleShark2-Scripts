from script_api import *

def AddExpReward(i):
    with Node("ExpReward " + str(i)):
        AddByte("Type") # 1 = meso, 2 = exp, 3 = prestige
        AddInt("Amount")

def AddItemReward(i):
    with Node("RewardItem " + str(i)):
        AddInt("ItemId")
        AddInt("Amount")
        AddInt("Rarity")
        AddByte("")
        AddByte("")
        AddByte("")


f = AddByte("function")
if f == 0: # dungeon reward
    AddByte("Unknown")
    AddInt("DungeonId")
    AddByte("Unknown")
    AddInt("Time? (s)")
    AddInt("Score?")
    AddInt("MaxScore?")
    AddByte("Unknown")
    AddByte("Unknown")
    AddByte("Unknown")
    AddByte("Unknown")
    a = AddInt("RewardCount")
    for i in range(a):
        AddExpReward(i)
    b = AddInt("RewardItemCount")
    for i in range(b):
        AddItemReward(i)
    c = AddInt("ExtraRewardCount")
    for i in range(c):
        AddExpReward(i)
    d = AddInt("ExtraRewardItemCount")
    for i in range(d):
        AddItemReward(i)
elif f == 1: # minigame reward
    AddInt("ClearedRounds")
    AddInt("LastRound")
    AddInt("FirstRound")
    AddExpReward(0)
    count = AddInt("RewardCount")
    for i in range(count):
        AddItemReward(i)

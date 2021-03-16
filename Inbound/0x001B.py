from script_api import *

def add_exp_reward(i):
    with Node("ExpReward " + str(i)):
        add_byte("Type") # 1 = meso, 2 = exp, 3 = prestige
        add_int("Amount")

def add_item_reward(i):
    with Node("RewardItem " + str(i)):
        add_int("ItemId")
        add_int("Amount")
        add_int("Rarity")
        add_byte("")
        add_byte("")
        add_byte("")


f = add_byte("function")
if f == 0: # dungeon reward
    add_byte("Unknown")
    add_int("DungeonId")
    add_byte("Unknown")
    add_int("Time? (s)")
    add_int("Score?")
    add_int("MaxScore?")
    add_byte("Unknown")
    add_byte("Unknown")
    add_byte("Unknown")
    add_byte("Unknown")
    a = add_int("RewardCount")
    for i in range(a):
        add_exp_reward(i)
    b = add_int("RewardItemCount")
    for i in range(b):
        add_item_reward(i)
    c = add_int("ExtraRewardCount")
    for i in range(c):
        add_exp_reward(i)
    d = add_int("ExtraRewardItemCount")
    for i in range(d):
        add_item_reward(i)
elif f == 1: # minigame reward
    add_int("ClearedRounds")
    add_int("LastRound")
    add_int("FirstRound")
    add_exp_reward(0)
    count = add_int("RewardCount")
    for i in range(count):
        add_item_reward(i)

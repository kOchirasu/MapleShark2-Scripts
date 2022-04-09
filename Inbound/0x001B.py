''' DUNGEON_REWARD '''
from script_api import *

def add_value_reward(i):
    with Node("ValueReward " + str(i)):
        add_byte("Type") # 1 = meso, 2 = exp, 3 = prestige
        add_int("Amount")

def add_item_reward(i):
    with Node("ItemEntity " + str(i)):
        add_int("ItemId")
        add_int("Amount")
        add_int("Rarity")
        add_byte("")
        add_byte("")
        add_byte("")

def add_reward(type):
    with Node(type):
        count = add_int("RewardCount")
        for i in range(count):
            add_reward(i)
        count = add_int("RewardItemCount")
        for i in range(count):
            add_item_reward(i)


f = add_byte("function")
if f == 0: # dungeon reward
    add_bool("Unknown")
    add_int("DungeonId")
    add_bool("Unknown")
    add_int("Time? (s)")
    add_int("Score?")
    add_int("MaxScore?")
    for i in range(4):
        add_byte("Unknown")

    add_reward("Reward")
    add_reward("ExtraReward")
elif f == 1: # minigame reward
    add_int("ClearedRounds")
    add_int("TotalRounds")
    add_reward("Reward")
elif f == 2:
    add_reward("Reward")
elif f == 3:
    add_bool("unknown")
    add_reward("Reward")
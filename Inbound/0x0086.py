from script_api import *

def DecodeWorldBoss():
    b = AddBool("Unknown")
    if b:
        count = AddInt("Count")
        for i in range(count):
            with Node("WorldBosses " + str(i)):
                entryCount = AddInt("Count")
                for j in range(entryCount):
                    with Node("WorldBossSpawn " + str(j)):
                        AddInt("MonsterId")
                        AddInt("MapId")
                        AddShort("Channel")
                        AddLong("SpawnTime?")
                        AddByte("Unknown (1)")

def DecodeMapPopulation():
    t = AddByte("PopulationType?")
    if t == 3:
        count = AddInt("Count")
        for i in range(count):
            with Node("MapPopulation " + str(i)):
                AddInt("MapId")
                # 1 = 3 icon, 2 = 2 icon, 3 = 1 icon
                AddInt("Population")
                AddShort("Channel")


f = AddByte("Function")
if f == 0:
    DecodeWorldBoss()
    b = AddBool("Unknown")
    if b:
        DecodeWorldBoss()
    b = AddByte("GetMapPopulation")
    with Node("MapPopulations"):
        if b == 1:
            DecodeMapPopulation()
elif f == 1:
    DecodeMapPopulation()

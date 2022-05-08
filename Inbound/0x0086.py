''' WORLD_MAP '''
from script_api import *

def decode_world_boss():
    b = add_bool("Unknown")
    if b:
        count = add_int("Count")
        for i in range(count):
            with Node("WorldBosses " + str(i)):
                entryCount = add_int("Count")
                for j in range(entryCount):
                    with Node("WorldBossSpawn " + str(j)):
                        add_int("MonsterId")
                        add_int("MapId")
                        add_short("Channel")
                        add_long("SpawnTime?")
                        add_byte("Unknown (1)")

def decode_map_population():
    t = add_byte("PopulationType?")
    if t == 3:
        count = add_int("Count")
        for i in range(count):
            with Node("MapPopulation " + str(i)):
                add_int("MapId")
                # 1 = 3 icon, 2 = 2 icon, 3 = 1 icon
                add_int("Population")
                add_short("Channel")


f = add_byte("Function")
if f == 0:
    decode_world_boss()
    b = add_bool("Unknown")
    if b:
        decode_world_boss()
    b = add_byte("GetMapPopulation")
    with Node("MapPopulations"):
        if b == 1:
            decode_map_population()
elif f == 1:
    decode_map_population()

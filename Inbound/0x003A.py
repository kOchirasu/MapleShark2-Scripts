''' MESO '''
from script_api import *

mesos = add_long("Mesos") # new meso amount
pcbang = add_int("pcbang") 
''' Client will use new meso amount to decide if mesos were gained or consumed

if mesosGained >= 0 and (pcbang == 21 or pcbang == 60001):
    pass # s_msg_take_pcbang
if mesosGained < 0:
    pass # s_msg_consume_meso
'''

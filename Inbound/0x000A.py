''' LOGIN_RESULT '''
from script_api import *

code = add_byte("code") # 0x00 = success, 0x07 = restricted, 0x19 = timed out
add_int("Unknown")
add_unicode_str("BanReason")
add_long("AccountId")
add_long("SyncTime")
add_int("TimeOffset")
add_byte("TimeZone")
f = add_byte("blockType")
add_int("CONST (0)")
add_long("CONST (0)")
if f == 1: # permanent ban?
    add_long("Timestamp")
elif f == 2: # temp ban?
    add_long("Timestamps")
    add_long("CurrentTimestamp")
add_int("status? 2 (CONST)")

'''
if code == 0:
  pass # OK
if code == 1 or code == 2:
  pass # s_login_err_id
if code == 3:
  pass # s_login_err_pwd
if code == 4 or code == 5:
  pass # s_alreadyloginuser_response_kick
if code == 6:
  pass # s_login_err_full_server
if code == 7:
  pass # s_login_err_restrict
if code == 8:
  pass # s_login_err_db
if code == 10:
  pass # s_login_err_full_ch
if code == 11 or code == 12:
  pass # AuthFailed_Maintenance
if code == 14:
  pass # s_login_err_external_block_nsn
if code == 15:
  pass # s_login_err_external_block_ip
if code == 16:
  pass # s_login_err_check_passport
if code == 18:
  pass # s_login_err_alphatester
if code == 19:
  pass # s_login_err_main_atl
if code == 20:
  pass # s_login_err_auto_external_block
if code == 21:
  pass # s_login_err_session_error
if code == 22:
  pass # s_login_err_tencent_signature
if code == 24:
  pass # s_login_err_admin_ip
if code == 25:
  pass # s_login_err_nxa_ticket
if code == 26:
  pass # s_founderspack_need
'''
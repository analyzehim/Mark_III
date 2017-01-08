import sys
import time
import random
sys.path.insert(0, sys.path[0]+'\\proto')
from bot_proto import *
from common_proto import *
from vk_proto import *
from sqlite_proto import *
telebot = Telegram()
for user in vk_getfriendlist(telebot.VK_TOKEN, 9041600):
    try:
        sqlite_add(user.uid, str(user.first_name) + ' ' + str(user.last_name))
    except: print user.uid

if check_user(9041600):
    print 1
else:
    print 0

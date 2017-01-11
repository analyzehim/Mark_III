import sys
import time
import random
sys.path.insert(0, sys.path[0]+'\\proto')
from bot_proto import *
from common_proto import *
from vk_proto import *
from sqlite_proto import *
telebot = Telegram()


print check_user('26557')
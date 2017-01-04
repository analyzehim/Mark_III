# -*- coding: utf-8 -*-
import sys
import random
sys.path.insert(0, sys.path[0]+'\\proto')
from bot_proto import *
from common_proto import *
from vk_proto import *
'''
BOT_MODE
0 - standart


4 - exit
'''

BOT_MODE = 0
EXIT_MODE = False


def check_updates():
    parameters_list = telebot.get_updates()
    if EXIT_MODE:
        return 1
    if not parameters_list:
        return 0
    for parameters in parameters_list:
        if parameters[3] != ADMIN_ID:
            telebot.send_text(parameters[3], "Who the fuck is you?")
            continue
        run_command(*parameters)


def run_command(name, from_id, cmd, author_id, date):
    global BOT_MODE
    global EXIT_MODE

    if cmd == '/help':
        telebot.send_text(from_id, 'No help today. Sorry, %s' % name)

    elif cmd in ('Hello', 'hello', 'hi', 'Hi'):   # Say hello
        telebot.send_text(from_id, 'Hello, %s' % name)

    elif cmd == '/vk':
        vk_resp = vk_ping(telebot.VK_TOKEN)
        telebot.send_text(from_id, vk_resp)

    elif cmd == '/exit':
        telebot.send_text_with_keyboard(from_id, 'Shut down?', [["Yes", "No"]])
        BOT_MODE = 4

    elif BOT_MODE == 4 and cmd == 'Yes':
        telebot.send_text(from_id, 'Finish by user {0} on {1}'.format(name, telebot.host))
        EXIT_MODE = True

    else:
        log_event('No action')
        BOT_MODE = 0

if __name__ == "__main__":
    telebot = Telegram()
    telebot.send_text(ADMIN_ID, "Run on {0}".format(telebot.host))
    while True:
        try:

            if check_updates() != 1:
                time.sleep(telebot.Interval)
            else:
                sys.exit()
        except KeyboardInterrupt:
            print 'Interrupt by user..'
            break
        except Exception, e:
            log_event(str(e))

import sqlite3
import datetime
import time
from common_proto import *
from bot_const import getVKToken

con = sqlite3.connect('data/vk/vk.db')
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS `Users`
            (`vk_id` INTEGER PRIMARY KEY NOT NULL ,
            `name` VARCHAR(100));''')


def sqlite_add(vk_id, name):
    # print '''INSERT OR IGNORE  INTO  Users(vk_id, name) VALUES ({0}, '{1}')'''.format(vk_id, name)
    cur.execute('''INSERT OR IGNORE INTO  Users(vk_id, name) VALUES ({0}, '{1}')'''.format(vk_id, name))
    con.commit()


def check_user(vk_id):
    for row in cur.execute('''SELECT * FROM Users WHERE vk_id={0}'''.format(vk_id)):
        return row[1]
    return vk_id


def db_init(users_list):
    for user in users_list:
        try:
            sqlite_add(user.uid, str(user.first_name) + ' ' + str(user.last_name))
        except:
            log_event("DB_INIT ERROR with " + str(user.uid))



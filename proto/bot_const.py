#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import xml.etree.ElementTree as ET


ADMIN_ID = 74102915  # My ID
PIG_ID = 117797858
URL = 'https://api.telegram.org/bot'  # HTTP Bot API URL
PIG_LIST = ['cute', 'adorable', 'attractive',
            'beautiful', 'handsome', 'pretty',
            'gorgeous', 'lovely', 'foxy',
            'sexy', 'hot', 'babe']
CHAT_ID = 65


def getHeartBeatInterval():
    tree = ET.parse('config.xml')
    root = tree.getroot()
    interval = root.findall('heartbeat_interval')[0].text
    return int(interval)


def getToken():
    tree = ET.parse('config.xml')
    root = tree.getroot()
    TOKEN = root.findall('token')[0].text
    return TOKEN


def getInterval():
    tree = ET.parse('config.xml')
    root = tree.getroot()
    interval = float(root.findall('interval')[0].text)
    return interval


def getProxies():
    tree = ET.parse('config.xml')
    root = tree.getroot()
    proxy_url = root.findall('proxy')[0].text
    f = open("password.txt", "r")
    password = f.read()
    proxy_url = proxy_url.replace("PASSWORD", password)
    proxies = {
      "http": proxy_url,
      "https": proxy_url,
    }
    return proxies


def checkMode():
    import requests

    try:
            requests.get('https://www.ya.ru')
            return False
    except:
            proxies = getProxies()
            requests.get('https://www.ya.ru', proxies=proxies)
            return True


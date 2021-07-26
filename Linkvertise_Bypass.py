import requests
import json
import ctypes
import os
import time
ctypes.windll.kernel32.SetConsoleTitleW("Linkvertise: Ad-Link Bypasser!")
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
def Main():
    link = str(input("Enter your linkvertise link: "))
    bypass=requests.get("https://bypass.bot.nu/bypass2?url={}".format(link))
    success = bypass.json()['success']
    if success == False:
        cls()
        print("Not a valid linkvertise link")
    if success == True:
        destination = bypass.json()['destination']
        cls()
        print(destination)
        time.sleep(10)
if __name__ == '__main__':
    Main()

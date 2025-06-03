import os
import time

import colorama
import requests


def _exit():
    time.sleep(5)
    exit()


def check_hook(hook):
    info = requests.get(hook).text
    if "\"message\": \"Unknown Webhook\"" in info:
        return False
    return True


def main(webhook, name, delay, amount, message, hookDeleter):
    counter = 0
    inf = amount == "inf"
    while inf or counter < int(amount):
        try:
            data = requests.post(webhook, json={"content": str(message), "name": str(name),
                                                "avatar_url": "https://i.pinimg.com/736x/91/44/e3/9144e397aae211cc154f4b118dbb95de.jpg"})
            if data.status_code == 204:
                print(f"{colorama.Back.RED} {colorama.Fore.WHITE}[+] Sent{colorama.Back.RESET}")
            else:
                print(f"{colorama.Back.RED} {colorama.Fore.WHITE}[-] Fail{colorama.Back.RESET}")
        except:
            print()
        time.sleep(float(delay))
        counter += 1
    if hookDeleter.lower() == "y":
        requests.delete(webhook)
        print(f'{colorama.Fore.RED}webhook deleted')
    print(f'{colorama.Fore.GREEN}done...')


def initialize():
    print(rf"""{colorama.Fore.RED}
 ___    ___ ________  ___  ________   _________  ___  ________           ___  ___  ________  ________  ___  __       
|\  \  /  /|\   __  \|\  \|\   ___  \|\___   ___\\  \|\   ____\         |\  \|\  \|\   __  \|\   __  \|\  \|\  \     
\ \  \/  / | \  \|\  \ \  \ \  \\ \  \|___ \  \_\ \  \ \  \___|_        \ \  \\\  \ \  \|\  \ \  \|\  \ \  \/  /|_   
 \ \    / / \ \   __  \ \  \ \  \\ \  \   \ \  \ \ \  \ \_____  \        \ \   __  \ \  \\\  \ \  \\\  \ \   ___  \  
  /     \/   \ \  \ \  \ \  \ \  \\ \  \   \ \  \ \ \  \|____|\  \        \ \  \ \  \ \  \\\  \ \  \\\  \ \  \\ \  \ 
 /  /\   \    \ \__\ \__\ \__\ \__\\ \__\   \ \__\ \ \__\____\_\  \        \ \__\ \__\ \_______\ \_______\ \__\\ \__\
/__/ /\ __\    \|__|\|__|\|__|\|__| \|__|    \|__|  \|__|\_________\        \|__|\|__|\|_______|\|_______|\|__| \|__|
|__|/ \|__|                                             \|_________|                                                 
                                                                                                                                                                                                                                         
                                                      BY XAINTII      #sntz      #Feard & respected       #revshit
     """)
    webhook = input("webhook url dito baliw > ")
    name = input("webhook name > ")
    message = input("Enter a message > ")
    delay = input("Enter a delay [int/float] > ")
    amount = input("Enter an amount [int/inf] > ")
    hookDeleter = input("Delete webhook after spam? [Y/N] > ")
    try:
        delay = float(delay)
    except ValueError:
        _exit()
    if not check_hook(webhook) or (not amount.isdigit() and amount != "inf") or (
            hookDeleter.lower() != "y" and hookDeleter.lower() != "n"):
        _exit()
    else:
        main(webhook, name, delay, amount, message, hookDeleter)
        _exit()


if __name__ == '__main__':
    os.system('title XAINTI ON TOPP')
    os.system('cls' if os.name == "nt" else "clear")
    colorama.init()
    initialize()

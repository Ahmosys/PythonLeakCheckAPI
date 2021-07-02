import os
import sys

from leakcheck import LeakCheckAPI
from dotenv import load_dotenv
from colorama import Fore

load_dotenv()
api = LeakCheckAPI()
api.set_key(os.getenv("API_KEY_LEAK_CHECK"))


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def welcome_message():
    print(
        f"""{Fore.RED}
██▓    ▓█████ ▄▄▄       ██ ▄█▀ ▄████▄   ██░ ██ ▓█████  ▄████▄   ██ ▄█▀
▓██▒    ▓█   ▀▒████▄     ██▄█▒ ▒██▀ ▀█  ▓██░ ██▒▓█   ▀ ▒██▀ ▀█   ██▄█▒ 
▒██░    ▒███  ▒██  ▀█▄  ▓███▄░ ▒▓█    ▄ ▒██▀▀██░▒███   ▒▓█    ▄ ▓███▄░ 
▒██░    ▒▓█  ▄░██▄▄▄▄██ ▓██ █▄ ▒▓▓▄ ▄██▒░▓█ ░██ ▒▓█  ▄ ▒▓▓▄ ▄██▒▓██ █▄ 
░██████▒░▒████▒▓█   ▓██▒▒██▒ █▄▒ ▓███▀ ░░▓█▒░██▓░▒████▒▒ ▓███▀ ░▒██▒ █▄
░ ▒░▓  ░░░ ▒░ ░▒▒   ▓▒█░▒ ▒▒ ▓▒░ ░▒ ▒  ░ ▒ ░░▒░▒░░ ▒░ ░░ ░▒ ▒  ░▒ ▒▒ ▓▒
░ ░ ▒  ░ ░ ░  ░ ▒   ▒▒ ░░ ░▒ ▒░  ░  ▒    ▒ ░▒░ ░ ░ ░  ░  ░  ▒   ░ ░▒ ▒░
░ ░      ░    ░   ▒   ░ ░░ ░ ░         ░  ░░ ░   ░   ░        ░ ░░ ░ 
    ░  ░   ░  ░     ░  ░░  ░   ░ ░       ░  ░  ░   ░  ░░ ░      ░  ░   
                            ░                       ░               
                    {Fore.YELLOW}Developed by Ramses - Licence MIT{Fore.RED}
                
                        • 1 - Search by E-mail
                        • 2 - Search by Username
                        • 3 - Search by Keyword
        {Fore.RESET}"""
    )


def search(type: str = None, mode: str = None):
    try:
        clear()
        query = input(
            f"""{Fore.RED}*******************************************************
Remaining requests : {Fore.YELLOW}{api.getLimits()["checks"]}{Fore.RED} | IP Address : {Fore.YELLOW}{api.getIP()}{Fore.RED}
*******************************************************
\n{Fore.YELLOW}[🚀] Enter a/an {mode} >> {Fore.RESET}"""
        )
        clear()
        api.set_type(type)
        api.set_query(query)
        result = api.lookup()
        print("[🔥] Data found [🔥]")
        if not result:
            print(f"{Fore.RED}No data found for this {mode}.{Fore.RESET}")
        else:
            for element in result:
                print(
                    f"""{Fore.GREEN}
--------------------------------------------------
Data : {element["line"]}
Source : {"".join(element["sources"])}
Date : {element["last_breach"]}
--------------------------------------------------{Fore.RESET}"""
                )
    except AssertionError:
        print("\n[🚫] There is an error in your search, please check the syntax. [🚫]")

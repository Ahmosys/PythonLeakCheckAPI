#!/usr/bin/python3

import sys
import time

from ext import utility
from colorama import Fore


def run():
    on = True
    while on:
        try:
            if utility.is_connected():
                utility.clear()
                utility.welcome_message()
                choice = input(f"""{Fore.YELLOW}[🚀] Your choice >>  {Fore.RESET}""")
                if not choice.isdigit():
                    utility.clear()
                    print("[🚫] Please enter a number. [🚫]")
                elif choice == "1":
                    utility.search("email", "e-mail")
                    on = utility.choice_continue()
                elif choice == "2":
                    utility.search("login", "username")
                    on = utility.choice_continue()
                elif choice == "3":
                    utility.search("mass", "keyword")
                    on = utility.choice_continue()
                else:
                    utility.clear()
                    print("[🚫] Please make a choice between option 1, 2 or 3. [🚫]")
            else:
                utility.sprint("\n[🚫] Please check your internet connection, retry in 5 seconds... [🚫]")
                for i in range (1,6):
                    print(f"• {Fore.RED}{6 - i}{Fore.RESET} seconds left...")
                    time.sleep(1)
        except KeyboardInterrupt:
            print("\n\n[🛑] Stopping the script.")
            sys.exit()


if __name__ == "__main__":
    run()

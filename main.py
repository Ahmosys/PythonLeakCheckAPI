#!/usr/bin/python3

import sys

from ext import utility
from colorama import Fore


def run():
    on = True
    while on:
        try:
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
        except KeyboardInterrupt:
            print("\n\n[🛑] Stopping the script.")
            sys.exit()


if __name__ == "__main__":
    utility.clear()
    run()

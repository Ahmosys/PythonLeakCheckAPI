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
                on = choice_continue()
            elif choice == "2":
                utility.search("login", "username")
                on = choice_continue()
            elif choice == "3":
                utility.search("mass", "keyword")
                on = choice_continue()
            else:
                utility.clear()
                print("[🚫] Please make a choice between option 1, 2 or 3. [🚫]")
        except KeyboardInterrupt:
            print("\n\n[🛑] Stopping the script.")
            sys.exit()


def choice_continue():
    choice_user = input(
        f"""\nWould you want to continue searching ?
{Fore.YELLOW}[🚀] Enter Y(yes) or N(no) >> {Fore.RESET}"""
    )
    if choice_user.lower() not in ("y", "yes"):
        utility.clear()
        print(
            f"[🤙] {Fore.RED}G{Fore.YELLOW}o{Fore.GREEN}o{Fore.CYAN}d {Fore.MAGENTA}b{Fore.RED}y{Fore.YELLOW}e{Fore.GREEN}!{Fore.RESET}\n"
        )
        return False
    else:
        utility.clear()
        return True


if __name__ == "__main__":
    utility.clear()
    run()

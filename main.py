import sys
import colorama
import sqlite3
db = input("Enter data base name (should end with .db) : ")
if (db.endswith(".db")):
    print(f"{colorama.Fore.LIGHTYELLOW_EX} Connected {colorama.Style.RESET_ALL}")
else : 
    raise ValueError(f"{colorama.Fore.RED}Failed to connect {colorama.Style.RESET_ALL}")
connection = sqlite3.connect(db) 
while True : 
    print(f"{colorama.Fore.RED} Enter a number from below {colorama.Style.RESET_ALL}")
    print(f"{colorama.Fore.YELLOW} 1 - Database tables {colorama.Style.RESET_ALL}")
    print(f"{colorama.Fore.YELLOW} 2 - Database Selection")
    print(f"{colorama.Fore.RED} 3 - EXIT {colorama.Style.RESET_ALL}")
    num = int(input(f"{colorama.Fore.YELLOW} Enter a Number : {colorama.Style.RESET_ALL}"))
    if num ==3 :
        print(f"{colorama.Fore.LIGHTMAGENTA_EX} GOODBYE... {colorama.Style.RESET_ALL}")
        sys.exit()
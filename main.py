import sys
import colorama
import sqlite3
import time
db = input(f"{colorama.Fore.RED}Enter data base name (should end with .db) : {colorama.Style.RESET_ALL}")

if (db.endswith(".db")):
    print(f"{colorama.Fore.LIGHTYELLOW_EX} Connected {colorama.Style.RESET_ALL}")

else : 
    raise ValueError(f"{colorama.Fore.RED}Failed to connect {colorama.Style.RESET_ALL}")

connection = sqlite3.connect(db) 
tables_dict = {}
c = connection.cursor()
def main () :
    while True : 
        print(f"{colorama.Fore.RED} Enter a number from below {colorama.Style.RESET_ALL}")
        print(f"{colorama.Fore.YELLOW} 1 - Database tables {colorama.Style.RESET_ALL}")
        print(f"{colorama.Fore.YELLOW} 2 - Database Selection")
        print(f"{colorama.Fore .YELLOW} 3 - Full Schema {colorama.Style.RESET_ALL}")
        print(f"{colorama.Fore.RED} 4 - EXIT {colorama.Style.RESET_ALL}")
        num = int(input(f"{colorama.Fore.YELLOW} Enter a Number : {colorama.Style.RESET_ALL}"))
        if num == 1 : 
            get_tables()
            time.sleep(5)
        if num == 2 : 
            get_tables()
            intput_table = int(input(f"{colorama.Fore.CYAN}Enter table number of table you want to Select from (0 to exite) : {colorama.Style.RESET_ALL}"))
            if intput_table == 0 : sys.exit()
            print(f"{colorama.Fore.RED} Table Choosen : {tables_dict.get(intput_table)} {colorama.Style.RESET_ALL}")
            print(f"{colorama.Fore.LIGHTRED_EX}Coulnms : {colorama.Style.RESET_ALL}") 
            get_columns(intput_table)
            input_column = int(input(f"{colorama.Fore.BLUE}Enter Column number Or Coulmns numbers (0 to exite): {colorama.Style.RESET_ALL}"))
        if num == 3 : get_schema()
        if num ==4 :
            print(f"{colorama.Fore.LIGHTMAGENTA_EX} GOODBYE... {colorama.Style.RESET_ALL}")
            sys.exit()


def get_tables():
    c.execute("""SELECT name FROM sqlite_master WHERE type ='table' ;""")
    result = c.fetchall()
    counter = 1
    for i in result : 
        tables_dict[counter] = i[0]
        print(f"{colorama.Fore.LIGHTBLUE_EX} --{counter} {i[0]} {colorama.Style.RESET_ALL}")    
        counter = counter+1
def get_schema() :
    c.execute(""" SELECT sql
    FROM sqlite_master
    WHERE sql IS NOT NULL ;""")
    r = c.fetchall()
    for i in r : 
        print(f"{colorama.Fore.YELLOW} {i[0]} {colorama.Style.RESET_ALL}")
def get_columns(table_number):
    choosen_table = tables_dict.get(table_number)
    c.execute(f"PRAGMA table_info({choosen_table})")
    r = c.fetchall()
    counter = 1  
    for column in r : 
        print(f"{colorama.Fore.RED} --{counter} {column[1]} {colorama.Style.RESET_ALL}") 
        counter = counter+1

main()
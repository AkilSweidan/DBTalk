import sys
import colorama
import sqlite3
import time
from colorama import Fore , Style
db = input(f"{Fore.RED}Enter data base name (should end with .db) : {Style.RESET_ALL}")

if (db.endswith(".db")):
    print(f"{Fore.LIGHTYELLOW_EX} Connected {Style.RESET_ALL}")

else : 
    raise ValueError(f"{Fore.RED}Failed to connect {Style.RESET_ALL}")

connection = sqlite3.connect(db) 
tables_dict = {}
coulumns_dict_number_name = {}
coulumns_dict_number_type = {}
selected_column = ""
selected_columns =[]
intput_table=0
columns = ", ".join(selected_columns)
c = connection.cursor()
def main () :
    while True : 
        selected_columns =[]
        intput_table=0
        columns = ", ".join(selected_columns)
        print(f"{Fore.RED} Enter a number from below {Style.RESET_ALL}")
        print(f"{Fore.YELLOW} 1 - Database tables {Style.RESET_ALL}")
        print(f"{Fore.YELLOW} 2 - Database Selection")
        print(f"{Fore .YELLOW} 3 - Full Schema {Style.RESET_ALL}")
        print(f"{Fore.RED} 4 - EXIT {Style.RESET_ALL}")
        num = int(input(f"{Fore.YELLOW} Enter a Number : {Style.RESET_ALL}"))
        if num == 1 : 
            get_tables()
            time.sleep(5)
        if num == 2 : 
            get_tables()
            intput_table = int(input(f"{Fore.CYAN}Enter table number of table you want to Select from (0 to exite) : {Style.RESET_ALL}"))
            if intput_table == 0 : sys.exit()
            print(f"{Fore.RED} Table Choosen : {tables_dict.get(intput_table)} {Style.RESET_ALL}")
            print(f"{Fore.LIGHTRED_EX}Columns : {Style.RESET_ALL}") 
            get_columns(intput_table)
            input_columns_list = list(map(int, input(f"{Fore.BLUE}Enter column number Or columns numbers SPACES BETWEEN (-1 Select All and 0 to exite): {Style.RESET_ALL}").split()))
            if -1 in input_columns_list :
                selected_column = "*"
                print(f"{Fore.GREEN} All Columns that will be printed {Style.RESET_ALL}")
                c.execute(f"SELECT * FROM {tables_dict.get(intput_table)}")
                print_values(c.fetchall())
            else :
                counter = 1
                print(f"{Fore.BLUE}Selected Columns : {Style.RESET_ALL}")
                for number in input_columns_list : 
                    selected_columns.append(coulumns_dict_number_name.get(number))
                    print(f"{Fore.BLUE}--{counter} {coulumns_dict_number_name.get(number)} {Style.RESET_ALL}")
                    counter = counter+1
                columns = ", ".join(selected_columns)
                c.execute(f"SELECT {columns} FROM {tables_dict.get(intput_table)};")
                print_values(c.fetchall())
        if num == 3 : get_schema()
        if num ==4 :
            print(f"{Fore.LIGHTMAGENTA_EX} Exiting... {Style.RESET_ALL}")
            sys.exit()


def get_tables():
    c.execute("""SELECT name FROM sqlite_master WHERE type ='table' ;""")
    result = c.fetchall()
    counter = 1
    for i in result : 
        tables_dict[counter] = i[0]
        print(f"{Fore.LIGHTBLUE_EX} --{counter} {i[0]} {Style.RESET_ALL}")    
        counter = counter+1
def get_schema() :
    c.execute(""" SELECT sql
    FROM sqlite_master
    WHERE sql IS NOT NULL ;""")
    r = c.fetchall()
    for i in r : 
        print(f"{Fore.YELLOW} {i[0]} {Style.RESET_ALL}")
def get_columns(table_number):
    choosen_table = tables_dict.get(table_number)
    c.execute(f"PRAGMA table_info({choosen_table})")
    r = c.fetchall()
    counter = 1  
    for column in r : 
        print(f"{Fore.RED} --{counter} {column[1]} {Style.RESET_ALL}") 
        coulumns_dict_number_name[counter] =column[1]
        coulumns_dict_number_type[counter] = column[2] 
        counter = counter+1

def print_values(c : list) :
    for tuple in c : 
        print(tuple)
main()
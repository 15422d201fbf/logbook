import os, sys, math

#check sudo privileges
if not os.geteuid() == 0: sys.exit("You need to be root to perform this action.")


#global variables
global DATE
DATE = os.popen("date --iso-8601").read().strip()

global PATH
PATH = '/home/nathan/logbook/data/'

splitted_date = DATE.split("-")

global year, month, day
year, month, day = splitted_date[0], splitted_date[1], splitted_date[2]

global week
week = math.ceil(int(day) / 7)

global FULL_PATH
FULL_PATH = PATH + str(year) + '/' + str(month) + '/' + str(week) + '/'

def main():
    #check if file already exists
    if os.path.exists(FULL_PATH):
        if DATE in os.listdir(FULL_PATH):
            print("Today's logbook already exists. Modify / Delete / Read (1/2/3)\n")
            choice = int(input(": "))

            choice_dic = {1: modify, 2: delete, 3: read, 4: shutdown}
            choice_dict = choice_dic.get(choice, error)

            choice_dict()

        else:
            with open(FULL_PATH + DATE, 'w') as f:
                while True:
                    try:
                        content = str(input("Enter your logbook (pressing enter will skip 2 lines), press CTRL+C or CTRL+D to stop writing > "))
                        f.write(content + "\n\n")

                    except KeyboardInterrupt or EOFError:
                        f.close()
                        sys.exit(f"Logbook saved in {FULL_PATH}. \nRun the script again to modify/read/delete it...\n")

    else:
        #check if year exists, if not we have to create all the other folders. The following portion will make sure we have the proprer directory available.
        if not year in os.listdir('data'):
            os.mkdir(PATH + year)
            print(f"Created {year} folder in {PATH}")
            os.mkdir(PATH + year + '/' + month)
            print(f"Created {month} folder in {PATH}{year}")
            os.mkdir(PATH + year + '/' + month + '/' + str(week))
            print(f"Created {str(week)} folder in {PATH}{year}/{month}")
                
                    
        else:
            if not month in os.listdir(f'data/{year}'):
                os.mkdir(PATH + year + '/' + month)
                print(f"Created {month} folder in {PATH}{year}")
                os.mkdir(PATH + year + '/' + month + '/' + str(week))
                print(f"Created {str(week)} folder in {PATH}{year}/{month}")

            else:
                if not week in os.listdir(f'data/{year}/{month}'):
                    os.mkdir(PATH + year + '/' + month + '/' + str(week))
                    print(f"Created {str(week)} folder in {PATH}{year}/{month}")


        with open(FULL_PATH + DATE, 'w') as f:
                while True:
                    try:
                        content = str(input("Enter your logbook (pressing enter will skip 2 lines), press CTRL+C or CTRL+D to stop writing > "))
                        f.write(content + "\n\n")

                    except KeyboardInterrupt or EOFError:
                        f.close()
                        sys.exit(f"Logbook saved in {FULL_PATH}. \nRun the script again to modify/read/delete it...\n")




#other functions
def modify():
    os.system(f"open {FULL_PATH}/{DATE}")

def delete():
    os.system(f"rm -rf {FULL_PATH}/{DATE}")

def read():
    print(FULL_PATH + DATE + '\n')
    os.system(f"cat {FULL_PATH}/{DATE}")
    print("\n")


def shutdown():
    sys.exit("Quitting...\n")


def error():
    sys.exit("Please enter a correct value.")

if __name__ == "__main__":
    main()

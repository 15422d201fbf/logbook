import os, sys, math

#check sudo privileges
if not os.geteuid() == 0: sys.exit("You need to be root to run the script.")


#global variables
global DATE
DATE = os.popen("date --iso-8601").read().strip()

global PATH
PATH = '/home/nathan/logbook/data/'

global PATH_OBJ
PATH_OBJ = '/home/nathan/logbook/objectives/'

splitted_date = DATE.split("-")

global year, month, day
year, month, day = splitted_date[0], splitted_date[1], splitted_date[2]

global week
week = math.ceil(int(day) / 7)

global FULL_PATH
FULL_PATH = PATH + str(year) + '/' + str(month) + '/' + str(week) + '/'

global obj_year
obj_year = str(int(year) + 1)

def main():
    #objectives
    if not obj_year in os.listdir('objectives'):
        print("\nObjectives not filed yet; create objectives ? (1/0)")
        choice = int(input(": "))
        
        if choice == 1:
            os.mkdir(PATH_OBJ + obj_year)
            print(f"Created {obj_year} folder {PATH_OBJ}. \n")
            with open(PATH_OBJ + obj_year + f'/OBJECTIVES{obj_year}', 'w') as f:
                while True:
                    try:
                        objective = str(input("Please enter your objective (press CTRL+C or CTRL+D to stop writing): "))
                        f.write('- ' + objective + ' []'+ '\n')

                    except KeyboardInterrupt or EOFError:
                        f.close()
                        print("Objectives saved as {PATH_OBJ}{obj_year}/OBJECTIVES{obj_year} . ")
                        main()

        elif choice == 0:
            pass

        else:
            print("Please input a valid number...")
            main()

    else:
        read(f'{PATH_OBJ}{obj_year}/OBJECTIVES{obj_year}')


    #check if file already exists in data

    if os.path.exists(FULL_PATH):
        if DATE in os.listdir(FULL_PATH):
            print("""Today's logbook already exists.
            
            1/ Modify
            2/ Delete
            3/ Read
            4/ Modify objectives
            5/ Quit\n""")
            choice = int(input(": "))

            choice_dic = {1: modify, 2: delete, 3: read, 4: modify_obj, 5: shutdown}
            choice_dict = choice_dic.get(choice, error)
            param = FULL_PATH + DATE

            choice_dict(param if choice != 4 else PATH_OBJ+ obj_year + f'/OBJECTIVES{obj_year}')

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
def modify_obj(PATH):
    with open(PATH, 'r') as f:
        x = f.readlines()
        biggest = len(max(x))
        for j in range(len(x)):
            formatted = x[j].strip('\n')
            print(f'{j+1} {formatted:<{biggest}}')

        while True:
            try:
                to_modify = int(input("(Press CTRL+C to confirm): "))
                if not 1 <= to_modify <= len(x) + 1:
                    print('\nPlease enter a valid number.')
                    modify_obj(PATH)

                else:
                    x[to_modify-1].replace('[]', '[X]')

            except KeyboardInterrupt:
                print("Saving changes...\n")
                main()

    with open(PATH, 'w+') as f:
        f.write(x)
        f.close()

            
def modify(PATH):
    os.system(f"open {PATH}")

def delete(PATH):
    os.system(f"rm -rf {PATH}")

def read(PATH):
    print(PATH + '\n')
    os.system(f"cat {PATH}")
    print("\n")


def shutdown(dummyarg):
    sys.exit("Quitting...\n")


def error():
    sys.exit("Please enter a correct value.")

if __name__ == "__main__":
    main()

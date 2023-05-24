import os, sys, math

#check sudo privileges
if not os.geteuid() == 0: sys.exit("You need to be root to perform this action.")

global DATE
DATE = os.popen("date --iso-8601").read().strip()
print(DATE)
global PATH
PATH = '/home/yourname/logbook/data/'

def exists(x):
    rec_date = date.split('-')


#prompt main user choices
def main():
    if exists():
        print("Logbook already exists. Delete, Modify, Read, Quit (1/2/3/4)\n")
        choice = int(input(": "))

        choice_dic = {1: delete, 2: modify, 3: read, 4: shutdown}
        choice_dict = choice_dic.get(choice, error)
        choice_dict()

    else:
        with open(PATH + DATE, 'w') as f:
            content = str(input("\nWrite your logbook > "))
            f.write(content)
            #store with sort function
            sort_file_automatically(DATE)

        sys.exit("Logbook created.")


#create user functions:
def delete():
    #modify
    os.system(f"rm -rf {PATH}{DATE}") 

def modify():
    #modify
    os.system(f"open {PATH}{DATE}") 

def read():
    #modify
    file =  PATH + DATE
    print(file + "\n")
    os.system(f"cat {PATH}{DATE}")
    print("\n")


def sort_file_automatically():
    #check if year file exists
    splitted_date = DATE.split("-")
    year, month, day = splitted_date[0], splitted_date[1], splitted_date[2]
    week = math.ceil(day / 7)

    #check if year exists, if not we have to create all the other folders 
    if not year in os.listdir('data'):
        os.mkdir(PATH + year)
        print(f"Created {year} folder in {PATH}")
        os.mkdir(PATH + year + '/' + month)
        print(f"Created {month} folder in {PATH}{year}")
        os.mkdir(PATH + year + '/' + month + '/' + week)

    


def shutdown():
    sys.exit("Quitting...")


def error():
    sys.exit("Please enter a correct value.")

if __name__ == "__main__":
    main()

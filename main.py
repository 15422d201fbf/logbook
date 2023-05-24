import os, sys

#check sudo privileges
if not os.geteuid() == 0: sys.exit("You need to be root to perform this action.")

global DATE
DATE = os.popen("date --iso-8601").read().strip()
print(DATE)
global PATH
PATH = '/home/nathan/logbook/data/'

#check file exists functions
def exists():
    return DATE in os.listdir('data')

#prompt main user choices
def main():
    if exists():
        print("Logbook already exists. Delete, Modify, Read, Search, Quit (1/2/3/4,5)\n")
        choice = int(input(": "))

        choice_dic = {1: delete, 2: modify, 3: read, 4: search, 5: shutdown}
        choice_dict = choice_dic.get(choice, error)
        choice_dict()

    else:
        with open(PATH + DATE, 'w') as f:
            content = str(input("\nWrite your logbook > "))
            f.write(content)

        sys.exit("Logbook created.")


#create user functions:
def delete():
    os.system(f"rm -rf {PATH}{DATE}") 

def modify():
    os.system(f"open {PATH}{DATE}") 

def read():
    file =  PATH + DATE
    print(file + "\n")
    os.system(f"cat {PATH}{DATE}")
    print("\n")

def search():
    print("Group by, search with keyword (1/2)")
    choice = int(input("\n: "))

    if choice == 1:
        print("Group by: week, month, year (1/2/3)")
        sort = int(input("\n: "))
        if sort == 1:
            pass

        elif sort == 2:
            pass

        elif sort == 3:
            FILES = os.listdir('data')
            print(FILES)

        else:
            error()



def shutdown():
    sys.exit("Quitting...")


def error():
    sys.exit("Please enter a correct value.")

if __name__ == "__main__":
    main()

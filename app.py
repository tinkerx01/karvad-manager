import json
###############توابع کمکی###############
def loadJson():
    #read info from json file. convert into format that program can use.
    with open(p) as file:
        try:
            for i in file:
                file.load()
        except FileNotFoundError:
            print("no such file")

def writeIntoFile():
    #convert into json, write to file. if not exists. 
    print("failed to write")

def getinfo(field):
    #choose custom field to print msg and get input
    msg = "Enter karvand "
    print(msg + field, end = ": ")
    usr_inp = input()


#################توابع اصلی##################
def addKrvd(p):
    loadJson(p)
    print("Karvand added successfully")


def showKrvd(path):
    krvd_list = {}
    print(krvd_list)

def searchById(path):

def searchBySk(path):

def editKrvd(path):
    print("Changes saved.")


def deleteKrvd(path):
    
    sure = input("Are you sure?(y/n)")
    if sure == 'y':
        print("Karvand Deleted.")
    else:
        return


def reports(path):
    report = {}
    print(report)


p = "data/karvands.json"

while True:
    usr_choice = input("Please pick an option:\n" \
                       "1.add new karvand\n" \
                       "2.show all karvand\n" \
                       "3.search for karvand by id\n" \
                       "4.search for karvand by skill\n" \
                       "5.edit karvand info\n" \
                       "6.delete karvand\n" \
                       "7.report\n" \
                       "8.exit: ")
    if usr_choice == '1':
        addKrvd(p)
    elif usr_choice == '2':
        showKrvd(p)
    elif usr_choice == '3':
        searchById(p)    
    elif usr_choice == '4':
        searchBySk(p)
    elif usr_choice == '5':
        editKrvd()
    elif usr_choice == '6':
        deleteKrvd(p)
    elif usr_choice == '7':
        reports(p)
    elif usr_choice == '8':
        break
    else:
        print("Invalid input. Try again")
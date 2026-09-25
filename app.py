import json

def addKrvd(path):
    print("Karvand added successfully")


def showKrvd(path):
    krvd_list = {}
    print(krvd_list)


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
    usr_choice = input("Please pick an option:\n1.add new karvand\n2.show karvand info\n" \
    "3.edit karvand info\n4.delete karvand\n5.get a report\n6.exit ")
    if usr_choice == '6':
        break
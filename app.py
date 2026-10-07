import json
import os

###############توابع کمکی###############
def loadJson(path):
    
    # Load JSON data from the given path.
    # Returns the parsed data (dict or list), or an empty dict if the file
    # doesn't exist or is empty/corrupt.
    
    if not os.path.exists(path):
        print(f"File '{path}' not found. Starting with empty data.")
        return {}

    try:
        with open(path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except json.JSONDecodeError:
        print(f"File '{path}' is not valid JSON. Starting with empty data.")
        return {}
    except (IOError, OSError) as e:
        print(f"Error reading '{path}': {e}")
        return {}
    
def saveJson(path, data):
    #write data to a JSON file, creating parent directories if needed.
    parent = os.path.dirname(path)
    if parent:                                
        #skip when parent exists
        os.makedirs(parent, exist_ok=True)
    try:
        with open(path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=2)
    except (IOError, OSError) as e:
        print(f"Failed to write to '{path}': {e}")

def getInfo(field):
    #choose custom field to print msg and get input
    msg = "Enter karvand "
    print(msg + field, end = ": ")
    usr_inp = input()
    return usr_inp

def vfyName():
    for i in range(3):
        fname = getInfo(field="first name")
        if fname.isalpha():
            break
        print("Unsupported characters. Please try again.")

    for i in range(3):
        lname = getInfo(field="last name")
        if lname.isalpha():
            break
        print("Unsupported characters. Please try again.")
            
    name = fname.capitalize() + " " + lname.capitalize()
    return name

def vfyemail():
    email = getInfo(field="email")
    return email 

def nextId(data):
    krvd = data.get("karvands", [])
    if not krvd:
        return 1
    return max(k["id"] for k in krvd) + 1


#################توابع اصلی##################
def addKrvd(p):
    data = loadJson(p)

    if "bootcamp" not in data:
        data["bootcamp"] = {"title": "Karvand Python", "year": 2026}
    if "karvands" not in data:
        data["karvands"] = []

    new_krvd = {
        "full_name" : vfyName(),
        "email" : vfyemail(),
        "city" : getInfo(field= "city").capitalize(),
        "degree" : getInfo(field="degree").capitalize(),
        "major" : getInfo(field = "major").capitalize(),
        "id" : nextId(data)
    }
    data["karvands"].append(new_krvd)
    saveJson(p, data)
    print(f"Karvand {new_krvd['full_name']} added successfully. Here's Karvand ID: {new_krvd['id']}:")


def showKrvd(p):
    data = loadJson(p)
    if not data:
        print("nothing to show here.")
        return None
    for item in data["karvands"]:
        print(item)


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
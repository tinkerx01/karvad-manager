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
    valid: False
    for i in range(3):
        fname = getInfo(field="first name")
        if fname.isalpha():
            valid = True
            break
        print("Unsupported characters. Please try again.")

    for i in range(3):
        lname = getInfo(field="last name")
        if lname.isalpha():
            valid = True
            break
        print("Unsupported characters. Please try again.")
            
    name = fname.capitalize() + " " + lname.capitalize()
    return name, valid

# def vfyemail():
#     email = getInfo(field="email")
#     return email 

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

    #only validates name format
    #since the others could be easily 
    #handled using regex

    name, valid =  vfyName()
    if not valid:
        print("Too many invalid tries.")
        return
    new_krvd = {
        "full_name" :name,
        "email" : getInfo(field="email"),
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


def searchById(p):
    data = loadJson(p)
    if 'karvands' not in data:
        print("No karvand found.")
        return None
    usr_inpt = getInfo(field="id").strip()
    try:
        trgt_id = int(usr_inpt)
    except ValueError:
        print("id must be a number.")
        return None
        
    for karvand in data['karvands']:
        if karvand.get('id') == trgt_id:
            print(f"search result for id {trgt_id}:\n")
            for item in karvand.items():
                print(item)
            return None
    print(f"No karvand found with id {trgt_id}.")
    return None


def searchBySk(p):
    print("failed to search")
    return None


def editKrvd(p):
    #read file
    data = loadJson(p)
    #check if empty
    if 'karvands' not in data:
        print("No karvand found.")
        return None
    
    #get input and validate
    usr_inpt = getInfo(field="id").strip()
    try:
        trgt_id = int(usr_inpt)
    except ValueError:
        print("id must be a number.")
        return None
    #handling value absence intead of putting it for last line
    target = None
    for karvand in data["karvands"]:
        if karvand.get("id") == trgt_id:
            target = karvand
            break
    if target is None:
        print(f"No karvand found with id {trgt_id}.")
        return None
    
    #user can only change these
    editable = ["email", "city", "degree", "major"]
    #giving user a chance to quit
    print("\nPress Enter to keep the current value.\n")
    changes = {}
    #loop file info, find matching fields
    for field in editable:
        current = target.get(field, "")
        new_value = getInfo(field=f"{field}[{current}]").strip().capitalize()

        if new_value == "":
            continue  # keep current

        changes[field] = new_value

    if not changes:
        print("No changes made.")
        return target

    target.update(changes)
    saveJson(p, data)
    print(f"Karvand {target['id']} updated successfully.")
    return target


def deleteKrvd(p):
        #read file
    data = loadJson(p)
    #check if empty
    if 'karvands' not in data:
        print("No karvand found.")
        return None
    
    #get input and validate
    usr_inpt = getInfo(field="id").strip()
    try:
        trgt_id = int(usr_inpt)
    except ValueError:
        print("id must be a number.")
        return None
    #handling value absence intead of putting it for last line
    target = None
    for karvand in data["karvands"]:
        if karvand.get("id") == trgt_id:
            target = karvand
            break
    if target is None:
        print(f"No karvand found with id {trgt_id}.")
        return None
    
    print(f"About to delete: {target.get('full_name', 'Unknown')} (id {trgt_id})")

    sure = getInfo(field="'y' to confirm").strip().lower()
    if sure != "y":
        print("Delete cancelled.")
        return None

    # remove it and save
    data["karvands"].remove(target)
    saveJson(p, data)
    print(f"Karvand {trgt_id} deleted successfully.")
    return target

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
        editKrvd(p)
    elif usr_choice == '6':
        deleteKrvd(p)
    elif usr_choice == '7':
        reports(p)
    elif usr_choice == '8':
        break
    else:
        print("Invalid input. Try again")
# Orchid watering app!

import json
from datetime import date

#Program to print orchids and latest watering dates
with open("orchids.json") as f:
    data = json.load(f)

for k in data["orchid_details"]:
    x = len(k["dates"])
    print(k["name"], " was last watered on ", k["dates"][x-1])

while True: #Program loop
     
    def rewrite(data, filename="orchids.json"):
        """Rewrites data to JSON array""" 
        with open(filename,'w') as f: 
            json.dump(data, f, indent = 4)

    def add_orchid():
        """Takes user input, appends orchid name to array"""
        new_orchid = input("Enter name of orchid that you would like to add\n")

        with open('orchids.json') as f:
            data = json.load(f)
        
        temp = data["orchid_details"]

        y = {"name": new_orchid,
            "dates": []
            } # Python object to be appended

        temp.append(y)
        
        rewrite(data) 
        print(new_orchid + " has been added!")
        
    def add_watering():
        """Appends datetime to 'names' """
        water_event = input("Which plant got watered?\n")

        with open("orchids.json") as json_file:
            data = json.load(json_file)

            temp = data["orchid_details"]

            for key in temp:
                if (water_event == key["name"]): 
                    today = date.today()
                    key["dates"].append(today.strftime("%m/%d/%Y"))  #change current date to string

            rewrite(data)
            print(water_event + " has been updated!")
            return

    def remove_orchid():
        """Deletes a key value pair from array"""
        delete_orchid = input("Which orchid do you want to delete?\n")
        with open("orchids.json") as json_file:
            data = json.load(json_file)

            temp = data["orchid_details"]

            for key in temp:
                if (delete_orchid == key["name"]):
                    temp.remove(key)

            rewrite(data)
            print(delete_orchid + " has been removed.")
            return

    def watering_history():
        """Takes user input, prints orchid's watering history"""
        who_water = input("Whose watering history do you want to see?\n")

        with open('orchids.json') as f:
            data = json.load(f)

            temp = data["orchid_details"]

            for x in temp:
                if(who_water == x["name"]):
                    for y in x["dates"]:
                        print(y)
        return

    #Menu options
    anything_else = input("\nWould you like to...?\n1. Add an orchid\n2. Add a watering\n3. Remove an orchid\n4. View an orchid's watering history\n")

    if anything_else == "1":
        add_orchid()

    elif anything_else == "2":
        add_watering()

    elif anything_else == "3":
        remove_orchid()

    elif anything_else == "4":
        watering_history()

    else:
        print("Enter a number 1-4.")

    #Ask if user wants to do anything else, otherwise exit program
    go_again = input("Would you like to do anything else?\n")
    if go_again.lower() != "yes":
        break

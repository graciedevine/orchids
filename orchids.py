import json
from datetime import date


def load():
    """Opens JSON file as Python object."""
    with open('orchids.json') as f:
        orchid_array = json.load(f)
        return orchid_array


orchid_data = load()


def rewrite(orchid_data, filename="orchids.json"):
    """Rewrites data to JSON array"""
    with open(filename, 'w') as f:
        json.dump(orchid_data, f, indent=4)


def add_orchid():
    """Adds a new entry to array."""
    new_orchid = input("Who would you like to add?\n")

    d = {"name": new_orchid,
         "dates": []
         }  # Python object to be appended.

    orchid_data.append(d)
    rewrite(orchid_data)
    print(new_orchid + " has been added!")


def add_watering():
    """Appends watering event to orchid."""
    water_event = input("Which plant got watered?\n")

    for d in orchid_data:
        if water_event == d["name"]:
            today = date.today()
            d["dates"].append(today.strftime("%m/%d/%Y"))  # change current date to string.
    rewrite(orchid_data)
    print(water_event + " has been updated!")


def remove_orchid():
    """Deletes an entry from array."""
    delete_orchid = input("Which orchid do you want to delete?\n")

    for d in orchid_data:
        if delete_orchid == d["name"]:
            orchid_data.remove(d)
    rewrite(orchid_data)
    print(delete_orchid + " has been removed.")


def watering_history():
    """Prints all of an orchid's watering dates."""
    who_water = input("Whose watering history do you want to see?\n")

    for x in orchid_data:
        if who_water == x["name"]:
            for y in x["dates"]:
                print(y)


# Print the latest watering dates of orchids.
for d in orchid_data:
    x = len(d["dates"])
    print(d["name"], " was last watered on ", d["dates"][-1])

while True:  # Menu options loop.
    anything_else = input(
        "\nWould you like to...?\n1. Add an orchid\n2. Add a watering\n"
        "3. Remove an orchid\n4. View an orchid's watering history\n")

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

    # Ask if user wants to do anything else, otherwise exit program.
    go_again = input("Would you like to do anything else? (y/n)\n")
    if go_again.lower() != "y":
        break

import json


def show_title():
    print("==============================")
    print("     AI PROFILE MANAGER")
    print("==============================")


def create_profile():
    name = input("What is your name? ")
    career = input("What is your career? ")
    experience = int(input("How many years experience do you have? "))
    goal = input("What is your AI learning goal? ")

    profile = {
        "name": name,
        "career": career,
        "experience": experience,
        "goal": goal
    }

    return profile

def save_profile(profile) :
    with open("user_profile.json", "w") as file:
        json.dump(profile, file, indent=4)
        print("profile saved successfully")

def load_profile():
    with open("user_profile.json","r") as file:
        profile = json.load(file)
        return profile

def show_menu():
    print("\nWhat would you like to do?")
    print("1. Create a new profile")
    print("2. View saved profile")
    print("3. Exit")

    

#start the program 

# start the program

show_title()

while True:
    show_menu()

    choice = input("Enter your choice (1, 2, or 3): ")

    if choice == "1":
        user_profile = create_profile()
        save_profile(user_profile)

        print("\nPROFILE CREATED")
        print(user_profile)

    elif choice == "2":
        loaded_profile = load_profile()

        print("\nSAVED PROFILE")
        print("Name:", loaded_profile["name"])
        print("Career:", loaded_profile["career"])
        print("Experience:", loaded_profile["experience"])
        print("AI Goal:", loaded_profile["goal"])

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")
        
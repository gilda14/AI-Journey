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


def save_profile(profile):
    with open("user_profile.json", "w") as file:
        json.dump(profile, file, indent=4)

    print("Profile saved successfully")


def load_profile():
    try:
        with open("user_profile.json", "r") as file:
            profile = json.load(file)

        return profile

    except FileNotFoundError:
        print("\nNo saved profile found.")
        return None


def edit_profile():
    profile = load_profile()

    if profile is None:
        return

    print("\nEDIT PROFILE")
    print("Press Enter to keep the current value.")

    print("\nCurrent name:", profile["name"])
    new_name = input("Enter new name: ")

    if new_name != "":
        profile["name"] = new_name

    print("\nCurrent career:", profile["career"])
    new_career = input("Enter new career: ")

    if new_career != "":
        profile["career"] = new_career

    print("\nCurrent experience:", profile["experience"])
    new_experience = input("Enter new years of experience: ")

    if new_experience != "":
        profile["experience"] = int(new_experience)

    print("\nCurrent AI goal:", profile["goal"])
    new_goal = input("Enter new AI goal: ")

    if new_goal != "":
        profile["goal"] = new_goal

    save_profile(profile)

    print("\nPROFILE UPDATED SUCCESSFULLY")


def show_menu():
    print("\nWhat would you like to do?")
    print("1. Create a new profile")
    print("2. View saved profile")
    print("3. Edit saved profile")
    print("4. Exit")


# Start the program

show_title()

while True:
    show_menu()

    choice = input("Enter your choice (1, 2, 3, or 4): ")

    if choice == "1":
        user_profile = create_profile()
        save_profile(user_profile)

        print("\nPROFILE CREATED")
        print(user_profile)

    elif choice == "2":
        loaded_profile = load_profile()

        if loaded_profile is not None:
            print("\nSAVED PROFILE")
            print("Name:", loaded_profile["name"])
            print("Career:", loaded_profile["career"])
            print("Experience:", loaded_profile["experience"])
            print("AI Goal:", loaded_profile["goal"])

    elif choice == "3":
        edit_profile()

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")
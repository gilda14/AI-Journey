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

#start the program 

show_title()
user_profile = create_profile()
print("\nPROFILE CREATE")
print(user_profile)

save_profile(user_profile)
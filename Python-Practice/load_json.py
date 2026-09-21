import json
with open("profile.json" , "r") as file :
    profile = json.load(file)

print("Profile loaded")
print(f"Name: {profile['name']}")
print(f"Career: {profile['career']}")
print(f"Experience: {profile['experience']}")
print(f"Goal: {profile['goal']}")
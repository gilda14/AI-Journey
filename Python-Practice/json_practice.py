import json

profile = {"name" : "admin",
          "career": "Business Owner",
          "experience": 20,
          "goal": "Learn AI"}
#open (file name , w = write mode)
with open("profile.json","w") as file :
    json.dump(profile, file, indent=4) #convert to the JSON
    print ("profile saved successfully")
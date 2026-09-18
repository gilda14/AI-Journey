# FUNCTION 1 - Show the program title

def show_title():
    print("==============================")
    print("      MY AI LEARNING JOURNEY")
    print("==============================")


# FUNCTION 2 - Show the user's profile

def show_profile(name, career, experience):
    print("\nYOUR PROFILE")
    print(f"Name: {name}")
    print(f"Career: {career}")
    print(f"Experience: {experience} years")


# START THE PROGRAM

show_title()


# ASK THE USER FOR INFORMATION

name = input("What is your name? ")

career = input("What is your career? ")

experience = int(input("How many years experience do you have? "))

technology = input("What do you want to learn? ")


# CREATE A LIST OF TECHNOLOGIES

technologies = ["Python", "HTML", "CSS", "JavaScript"]


# ADD REACT TO THE LIST

technologies.append("React")


# ASK FOR FUTURE GOAL

goal = input("What is your future goal? ")


# CALCULATE NEXT YEAR'S EXPERIENCE

next_year_experience = experience + 1


# ASK FOR ANOTHER TECHNOLOGY

new_technology = input("Enter a new skill that you want to learn: ")


# ADD THE NEW TECHNOLOGY TO THE LIST

technologies.append(new_technology)


# DISPLAY THE UPDATED TECHNOLOGY LIST

print("\nUpdated technology list:")

for technology in technologies:
    print(f"- {technology}")


# CALL OUR SECOND FUNCTION

show_profile(name, career, experience)


# COUNT THE TECHNOLOGIES

number_of_technologies = len(technologies)

print(f"\nI am learning {number_of_technologies} technologies.")


# DISPLAY EACH TECHNOLOGY

for technology in technologies:
    print(f"I am learning {technology}")


# DISPLAY FUTURE GOAL

print(f"\nMy future goal: {goal}")


# DISPLAY NEXT YEAR'S EXPERIENCE

print(
    f"Next year you will have {next_year_experience} years of experience."
)


# CHECK EXPERIENCE LEVEL

if experience >= 10:
    print("You are very experienced.")

elif experience >= 5:
    print("You can do it, but you should continue working hard.")

else:
    print(
        "You have to practise a lot. "
        "You are continuing to build your professional experience."
    )
    
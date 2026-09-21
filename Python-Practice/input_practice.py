# ==========================================
# FUNCTION 1 - SHOW THE PROGRAM TITLE
# ==========================================

def show_title():
    print("==============================")
    print("      MY AI LEARNING JOURNEY")
    print("==============================")


# ==========================================
# FUNCTION 2 - SHOW THE USER'S PROFILE
# ==========================================

def show_profile(name, career, experience):
    print("\nYOUR PROFILE")
    print(f"Name: {name}")
    print(f"Career: {career}")
    print(f"Experience: {experience} years")


# ==========================================
# FUNCTION 3 - CHECK EXPERIENCE LEVEL
# ==========================================

def get_experience_level(experience):
    if experience >= 10:
        return "Expert"

    elif experience >= 5:
        return "Intermediate"

    else:
        return "Beginner"


# ==========================================
# FUNCTION 4 - CALCULATE NEXT YEAR'S EXPERIENCE
# ==========================================

def calculate_next_year_experience(experience):
    next_year = experience + 1
    return next_year


# ==========================================
# START THE PROGRAM
# ==========================================

show_title()


# ==========================================
# ASK THE USER FOR INFORMATION
# ==========================================

name = input("What is your name? ")

career = input("What is your career? ")

experience = int(
    input("How many years experience do you have? ")
)

technology = input("What do you want to learn? ")


# ==========================================
# CALL FUNCTION 3 - GET EXPERIENCE LEVEL
# ==========================================

experience_level = get_experience_level(experience)

print(f"Your experience level is: {experience_level}")


# ==========================================
# CALL FUNCTION 4 - CALCULATE NEXT YEAR
# ==========================================

next_year_experience = calculate_next_year_experience(experience)


# ==========================================
# CREATE A LIST OF TECHNOLOGIES
# ==========================================

technologies = [
    "Python",
    "HTML",
    "CSS",
    "JavaScript"
]


# ADD REACT TO THE LIST

technologies.append("React")


# ==========================================
# ASK FOR FUTURE GOAL
# ==========================================

goal = input("What is your future goal? ")


# ==========================================
# ASK FOR ANOTHER TECHNOLOGY
# ==========================================

new_technology = input(
    "Enter a new skill that you want to learn: "
)


# ADD THE NEW TECHNOLOGY TO THE LIST

technologies.append(new_technology)


# ==========================================
# DISPLAY THE UPDATED TECHNOLOGY LIST
# ==========================================

print("\nUpdated technology list:")

for technology in technologies:
    print(f"- {technology}")


# ==========================================
# CALL FUNCTION 2 - SHOW USER PROFILE
# ==========================================

show_profile(name, career, experience)


# ==========================================
# COUNT THE TECHNOLOGIES
# ==========================================

number_of_technologies = len(technologies)

print(
    f"\nI am learning {number_of_technologies} technologies."
)


# ==========================================
# DISPLAY EACH TECHNOLOGY
# ==========================================

for technology in technologies:
    print(f"I am learning {technology}")


# ==========================================
# DISPLAY FUTURE GOAL
# ==========================================

print(f"\nMy future goal: {goal}")


# ==========================================
# DISPLAY NEXT YEAR'S EXPERIENCE
# ==========================================

print(
    f"Next year you will have "
    f"{next_year_experience} years of experience."
)


# ==========================================
# DISPLAY EXPERIENCE LEVEL
# ==========================================

print(f"Your experience level is: {experience_level}")
name = input("what is your name?")
career = input ("what is your career ?")
experience = int(input("how many years experience do you have?"))
technology = input("what do you want to learn?")
technologies = ["Python", "HTML", "CSS", "JavaScript"]
goal =input("what is your furture goal?")
next_year_experience = experience +1

print(f"name :{name}")
print (f"Career: {career}")
print (f"Experience : {experience} years ")
print(f"Current learning: {technology}")
print(technologies)
print(f"my future goal :{goal}")
print (f"next year you will have {next_year_experience} years of experience")
if experience >=10: print("you are expert") 
elif experience >=5:
    print ("you can do it but you should work hard  ")
else:
    print (" you have to practice alot, you are continuing to build your professional experience ")
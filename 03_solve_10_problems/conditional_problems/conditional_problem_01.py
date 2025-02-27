# 1. Age Group Categorization:
# Classify a person's age group: Child (< 13), Teenager (13-19), Adult (20-59), Senior (60+).

userAge = input("Enter your age : ")
age = int(userAge)

if age < 13:
    print("You are child !")
elif age >=13 and age <=19:
    print("You are Teenager !")
elif age >=20 and age <=59:
    print("You are Adult !")
else:
    print("You are Senior !")


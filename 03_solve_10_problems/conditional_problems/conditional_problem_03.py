# ▼3. Grade Calculator
# Problem: Assign a letter grade based on a student's score: A (90-100), B (80-89), C (70-79),
# D (60-69), F (below 60).

userScore = int(input("Enter your score: "))
if userScore < 101 and userScore > -1:
    if userScore >= 90 and userScore <= 100:
        print("Your Grade is A due to your score:", userScore)
    elif userScore >= 80 and userScore <= 89:
        print("Your Grade is B due to your score:", userScore)
    elif userScore >= 70 and userScore <= 79:
        print("Your Grade is C due to your score:", userScore)
    elif userScore >= 60 and userScore <= 69:
        print("Your Grade is D due to your score:", userScore)
    else:
        print("Your Grade is F due to your score:", userScore)
else:
    print("Please Enter Valid Score!!!")


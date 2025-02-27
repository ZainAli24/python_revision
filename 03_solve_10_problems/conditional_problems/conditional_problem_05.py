# 5. Weather Activity Suggestion
# Problem: Suggest an activity based on the weather 
# (e.g., Sunny - Go for a walk, Rainy - Read a book, Snowy - Build a snowman).

weather = input("Enter today weather: ")

userWeather = weather.lower()

if userWeather in ["sunny" , "rainy" , "snowy"]:
    if userWeather == "sunny":
        print("It's a beautiful sunny day! Go for a walk and enjoy the sunshine.")
    elif userWeather == "rainy":
        print("It's raining outside! Grab a book and enjoy the cozy weather.")
    elif userWeather == "snowy":
        print("It's a snowy day! Have fun building a snowman and playing with snowballs.")
else:
    print(f"Sorry, I don't have information about this weather: {userWeather}.")

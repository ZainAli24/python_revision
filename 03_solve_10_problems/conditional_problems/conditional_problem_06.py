# ▼6. Transportation Mode Selection
# Problem: Choose a mode of transportation based on the distance 
# (e.g., <3 km: Walk, 3-15 km: Bike, >15 km: Car).

userDis = int(input("Enter your distance: "))

if userDis < 3:
    print("Since the distance is short, walking is the best option for you.")
elif userDis >= 3 and userDis <=15:
    print("A bike would be a great choice for this distance—it's fast and efficient!")
elif userDis > 15:
    print("Since the distance is long, using a car would be the most comfortable option.")
else:
    print("Invalid input! Please enter a valid distance.")
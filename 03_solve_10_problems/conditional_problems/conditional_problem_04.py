# 4. Fruit Ripeness Checker
# Problem: Determine if a fruit is ripe, overripe, or unripe based on its color.
# (e.g., Banana: Green - Unripe, Yellow - Ripe, Brown - Overripe)

fruit = input("Enter your fruit: ")
fruitColor = input("Enter your fruit color: ")

fruitt = fruit.lower()
fruitCol = fruitColor.lower()

if fruitt not in ["banana", "apple"]:
    print("Invalid fruit! Please enter a valid fruit.")
elif fruitCol not in ["green", "yellow", "brown"]:
    print("Invalid color! Please enter a valid color.")
else:
    if fruitCol == "green":
        print(f"Your {fruitt} is unripe based on its color {fruitCol}.")
    elif fruitCol == "yellow":
        print(f"Your {fruitt} is ripe based on its color {fruitCol}.")
    elif fruitCol == "brown":
        print(f"Your {fruitt} is overripe based on its color {fruitCol}.")

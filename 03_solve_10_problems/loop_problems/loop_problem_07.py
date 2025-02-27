# ▼7. Validate Input
# Problem: Keep asking the user for input until they enter a number between 1 and 10.

while True:
    user_num = int(input("Enter a number: "))

    if 1 <= user_num <= 10:
        print("Thanks")
        break
    else:
        print("Plase Enter Valid number , try again!")


# 7. Coffee Customization
# Problem: Customize a coffee order: "Small", "Medium", or "Large" with an option for "Extra shot" 
# of espresso.

userorder = input("Enter your ordered coffee size: ")
order = userorder.lower()
Extrashot = False

userchoice = int(input("Do you want an extra shot of espresso? \n 1. Yes \n 2. No \nEnter your choice (1 or 2): "))
if userchoice == 1:
    Extrashot = True
if userchoice == 2:
    Extrashot == False
else:
    print("Please select one option from 1 and 2")


if order in ["small" , "medium" , "large"]:
    if Extrashot:
        print(f"You have ordered a {order} coffee with an extra shot of espresso. Enjoy!")
    else:
        print(f"You have ordered a {order} coffee. Enjoy your drink!")
else:
    print("Invalid size! Please choose from Small, Medium, or Large.")

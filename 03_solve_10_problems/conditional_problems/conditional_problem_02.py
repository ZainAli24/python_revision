# ▼2. Movie Ticket Pricing
# Problem: Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children. Everyone
# gets a $2 discount on Wednesday.

userAge = int(input("Enter your age: "))
userDay = (input("Enter today day : " ))
day = userDay.upper()

price = 12 if userAge >= 18 else 8

if day == "WEDNESDAY":
    # price = price - 2
    price -= 2

print(f"Ticket price for you is ${price}")

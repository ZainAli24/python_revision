# ▼9. Leap Year Checker
# Problem: Determine if a year is a leap year.
# (Leap years are divisible by 4, but not by 100 unless also divisible by 400).

useryear = int(input("Enter a year to check if it is a leap year: "))

if (useryear % 400 == 0) or (useryear % 4 == 0 and useryear % 100 != 0):
    print(f"Yes! {useryear} is a leap year. 🎉")
else:
    print(f"No, {useryear} is not a leap year.")

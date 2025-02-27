# ▼6. Factorial Calculator
# Problem: Compute the factorial of a number using a while loop.

user_num = int(input("Enter a number for factorial:  "))
original_num = user_num
factorial = 1

while user_num > 0:
    factorial = factorial * user_num
    user_num = user_num - 1
print(f"Factorial of {original_num} is {factorial}")

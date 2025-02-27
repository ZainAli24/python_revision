# 2. Sum of Even Numbers
# Problem: Calculate the sum of even numbers up to a given number n.

n = int(input("Enter a positive number up to which you want even numbers: "))

sum_even_number = 0

for m in range(0 , n+1):
    if m % 2 == 0:
        print(f"{m} is even number")
        sum_even_number += 1
print(f"Sum of even number from 0 to {n} is {sum_even_number}")

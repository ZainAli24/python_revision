# ▼3. Multiplication Table Printer
# Problem: Print the multiplication table for a given number up to 10, but skip the fifth iteration.

user_num =  int(input("Enter a number to print its multiplication table: "))

for num in range(1, 11):
    if num != 5:
        print(f"{user_num} x {num}  =  {user_num * num}")
    else:
        continue

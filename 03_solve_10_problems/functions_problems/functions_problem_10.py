# 10. Recursive Function
# Problem: Create a recursive function to calculate the factorial of a number.


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    

print(factorial(5))


# **Function Calls (Recursion):**  
#    - factorial(5) = 5 * result of factorial(4)  
#    - factorial(4) = 4 * result of factorial(3)  
#    - factorial(3) = 3 * result of factorial(2)  
#    - factorial(2) = 2 * result of factorial(1)  
#    - factorial(1) = 1 * result of factorial(0)  
#    - factorial(0) = 1 (Base case)

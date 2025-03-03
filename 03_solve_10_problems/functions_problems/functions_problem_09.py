# ▼9. Generator Function with yield
# Problem: Write a generator function that yields even numbers up to a specified limit.

# def even(num):
#     for n in range(1, num+1):
#         if n % 2 == 0:
#             print(f"{n} is even number")
#         else:
#             print(f"{n} is odd number")
#     return n

# print(even(11))


# 2. use of yield:
def even_generator(num):
    for n in range(2, num+1, 2):
        yield n


for num in even_generator(10):
    print(num)




# Is code ke andar jo "for" loop use ho raha hai, wo even numbers generate karne ke liye design kiya gaya hai. Chaliye step by step samajhte hain:
# 1. **Loop Ka Structure:**  
#    ```python
#    for n in range(2, num+1, 2):
#        return n
#    ```  
#    - `range(2, num+1, 2)` even numbers generate karta hai. Agar `num` 10 hai, to ye sequence hogi: 2, 4, 6, 8, 10.
   
# 2. **Return Statement:**  
#    - Lekin "return n" loop ke andar hai. Jaise hi loop ka pehla iteration execute hota hai (jab `n` ka value 2 hota hai), function "return n" execute karke value 2 return kar deta hai.
#    - Jab return statement call hota hai, function turant terminate ho jata hai aur baqi iterations (4, 6, 8, 10) kabhi execute nahi hoti.

# 3. **Result:**  
#    - Is wajah se, even_generator(10) sirf pehla even number (2) return karta hai, aur aapko baqi even numbers nahi milte.

# ### Agar Aap Multiple Values Chahein:
# Agar aap multiple even numbers return karna chahte hain, to aapko "yield" statement use karna chahiye. Jaise:

# ```python
# def even_generator(num):
#     for n in range(2, num+1, 2):
#         yield n

# for even in even_generator(10):
#     print(even)
# ```

# Is tarah se, "yield" har iteration ke baad value return karta hai, aur aapko 2, 4, 6, 8, 10 sab values milengi.

# ---

# **Summary:**  
# Aapka original code sirf pehla iteration execute hone ke baad return kar deta hai, isliye function se sirf ek hi value (2) milti hai.
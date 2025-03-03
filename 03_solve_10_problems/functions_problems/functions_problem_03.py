# 3. Polymorphism in Functions
# Problem: Write a function multiply that multiplies two numbers, but can also accept and multiply strings.

def multiply(a , b):
    return a * b


print(multiply(5 , 5))
print(multiply(2 , "SAMEER "))
res = multiply("ZAIN \n", 5)
print(res)



# Polymorphism ka matlab hai **"ایک چیز کے کئی روپ"**.  

# Programming mein polymorphism ka matlab hai ke ek function, method ya object mukhtalif tareeqon se kaam kar sakta hai. Matlab ek hi naam ka function ya method alag-alag tareeqon se behave kar sakta hai.  

# ### Example:
# Agar ek function **`calculate`** hai jo:
# - Do numbers ko **add** bhi kar sakta hai  
# - Aur strings ko **concatenate** bhi kar sakta hai  

# To ye **polymorphism** ka example hoga.  

# ### Real-life Example:
# Ek **"Mobile"** ka concept lein:
# - **Calling ke liye** use hota hai  
# - **Internet chalane ke liye** bhi use hota hai  
# - **Camera ki tarah** bhi kaam karta hai  

# Yani ek hi cheez mukhtalif tareeqon se behave kar sakti hai. Isi ko **polymorphism** kehte hain.
# Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
# >>> tea_varities = ["Black" , "Oolong" , "White" , "Green"]
# ['Black', 'Oolong', 'White', 'Green']
# Black
# >>> print(tea_varities[1])
# Oolong
# >>> print(tea_varities[-1])
# Green
# >>> print(tea_varities[1: 3])
# ['Oolong', 'White']
# >>> print(tea_varities[:2])
# ['Black', 'Oolong']
# >>> print(tea_varities[2:])
# ['White', 'Green']
# >>>
# >>> tea_varities
# ['Black', 'Oolong', 'White', 'Green']
# >>> tea_varities[3] = "Herbal"
# >>> print(tea_varities)
# ['Black', 'Oolong', 'White', 'Herbal']
# >>>
# >>> tea_varities[1:2] = "Lemon"
# >>> print(tea_varities)
# ['Black', 'L', 'e', 'm', 'o', 'n', 'White', 'Herbal']

# >>> tea_varities = ["Black" , "Oolong" , "White" , "Green"]
# >>> tea_varities[1:2] = ["Lemon"]
# >>> print(tea_varities)
# ['Black', 'Lemon', 'White', 'Green']
# >>>
# >>> tea_varities[1:3] = ["Mint" , "Herbal"]
# >>> print(tea_varities)
# ['Black', 'Mint', 'Herbal', 'Green']
# >>>
# >>> tea_varities
# ['Black', 'Oolong', 'White', 'Green']
# >>> tea_varities[1:1]
# []
# >>> tea_varities[1:1] = ["Ginger","Mint"]
# >>> tea_varities
# ['Black', 'Ginger', 'Mint', 'Oolong', 'White', 'Green']
# >>> tea_varities
# ['Black', 'Ginger', 'Mint', 'Masala', 'Pink']
# >>> tea_varities[1:3] = []
# >>> tea_varities
# ['Black', 'Masala', 'Pink']
# >>>
# >>> tea_varities
# ['Black', 'Ginger', 'Mint', 'Masala', 'Pink']
# >>> for tea in tea_varities:
# ...     print(tea)
# ...
# Black
# Ginger
# Mint
# Masala
# Pink
# >>>
# >>> for tea in tea_varities:
# ...     print(tea , end="-")
# ...
# Black-Ginger-Mint-Masala-Pink->>>
# >>>
# >>> tea_varities
# ['Black', 'Ginger', 'Mint', 'Masala', 'Pink']
# >>> if "Oolong" in tea_varities:
# ...     print("Oolong Tea")
# ...
# >>> tea_varities.append("Olong")
# >>> tea_varities
# ['Black', 'Ginger', 'Mint', 'Masala', 'Pink', 'Olong']
# >>> if "Olong" in tea_varities:
# ...     print("Oolong Tea")
# ...
# Oolong Tea
# >>>
# >>> tea_varities
# ['Black', 'Ginger', 'Mint', 'Masala', 'Pink', 'Olong']
# >>> tea_varities.pop()
# 'Olong'
# >>> tea_varities
# ['Black', 'Ginger', 'Mint', 'Masala', 'Pink']
# >>>
# >>> tea_varities
# ['Black', 'Ginger', 'Mint', 'Masala', 'Pink']
# >>> tea_varities.remove("Masala")
# >>> tea_varities
# ['Black', 'Ginger', 'Mint', 'Pink']
# >>>
# >>> tea_varities
# ['Black', 'Ginger', 'Mint', 'Pink']
# >>> tea_varities.insert(3, "Oolong")
# >>> tea_varities
# ['Black', 'Ginger', 'Mint', 'Oolong', 'Pink']
# >>>
# >>> tea_variety = tea_varities.copy()
# >>> tea_variety
# ['Black', 'Ginger', 'Mint', 'Oolong', 'Pink']
# >>> tea_varities.copy()
# ['Black', 'Ginger', 'Mint', 'Oolong', 'Pink']
# >>>
# >>> tea_variety
# ['Black', 'Ginger', 'Mint', 'Oolong', 'Pink']
# >>> tea_varities
# ['Black', 'Ginger', 'Mint', 'Oolong', 'Pink']
# >>> tea_varities.append("Cofee")
# >>> tea_varities
# ['Black', 'Ginger', 'Mint', 'Oolong', 'Pink', 'Cofee']
# >>> tea_variety
# ['Black', 'Ginger', 'Mint', 'Oolong', 'Pink']
# >>>
#________comprehension for loop :-
# >>>
# >>> squared_num = [x**2 for x in range(10)]
# >>> squared_num
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# >>> squared_num = [x**2 for x in range(11)]
# >>> squared_num
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# >>>
# Haan, bilkul sahi samjha!  

# ### **`[x**2 for x in range(10)]` ka Matlab:**  
# Ye ek **list comprehension** hai jo ek **loop** ki tarah kaam karta hai.  

# ### **Breakdown:**  
# 1. `range(10)` → **0 se 9 tak numbers generate karega** (10 include nahi hoga).  
# 2. `x**2` → **Har number ka square** le raha hai.  
# 3. **List me store kar raha hai.**  

# ### **Equivalent Loop Code:**  
# Agar **normal loop** se likhein to ye hoga:  
# ```python
# squared_num = []
# for x in range(10):
#     squared_num.append(x**2)
# ```

# **Output:**  
# ```python
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# ```

# Matlab **haan, ye loop hi hai jo har number ko square karke list me daal raha hai!** 

# >>> cube_num = [x**3 for x in range(10)]
# >>> cube_num
# [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]
# >>>

#--------------------------------------------------------------#

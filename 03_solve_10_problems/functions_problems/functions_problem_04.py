# ▼4. Function Returning Multiple Values
# Problem: Create a function that returns both the area and circumference of a circle given its radius.
import math

def circle(radius):
    area = math.pi * radius**2
    circumference = 2 * math.pi * radius
    return area, circumference


area, circum = circle(3)
print(f"Area = {area:.1f}")
print(f"Circumference = {circum:.1f}")



### **Area aur Circumference ka Matlab**  

# Agar **circle** (daira) ko samjhein, to uske **do important cheezen hoti hain:**  

# 1. **Area (رقبہ):**  
#    - Ye circle ke andar ka **total surface area** hota hai.  
#    - Formula: **π × r²**  
#    - (π ≈ 3.1416, r = radius)  

# 2. **Circumference (محیط):**  
#    - Ye circle ki **boundary ka total length** hota hai.  
#    - Formula: **2 × π × r**  

# ---

# ### **Example Function in Python:**
# ```python
# import math

# def circle_properties(radius):
#     area = math.pi * radius ** 2
#     circumference = 2 * math.pi * radius
#     return area, circumference

# # Example Usage:
# r = 5
# area, circumference = circle_properties(r)
# print(f"Area: {area}")
# print(f"Circumference: {circumference}")
# ```

# ✅ **Agar `radius = 5` ho, to output hoga:**  
# ```
# Area: 78.53981633974483  
# Circumference: 31.41592653589793  
# ```

# ---

# ### **Real-life Example:**  
# Agar aapke paas ek **gol table** hai aur aap uska **area** ya **boundary ka length** (circumference) nikalna chahte hain, to ye formulas use honge.
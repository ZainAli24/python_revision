# PS D:\python_revision\02_DataTypes> python
# Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> chai_types = {'name': 'Zain', 'age': 'Twenty one', 'gender': 'male'}
# >>> chai_types
# {'name': 'Zain', 'age': 'Twenty one', 'gender': 'male'}
# >>> chai_types['name']
# 'Zain'
# >>> chai_types.get('age')
# 'Twenty one'
# >>> chai_types.get('ager')
# >>> chai_types.['ager']
#   File "<stdin>", line 1
#     chai_types.['ager']
#                ^
# SyntaxError: invalid syntax
# >>>
# >>> chai_types['age'] = 'Ninety'
# >>> chai_types
# {'name': 'Zain', 'age': 'Ninety', 'gender': 'male'}
# >>>

# >>> chai_types
# {'name': 'Zain', 'age': 'Ninety', 'gender': 'male'}
# >>> for chai in chai_types:
# ...     print(chai)
# ...
# name
# age
# gender
# >>> for chai in chai_types:
# ...     print(chai, chai_types[chai])
# ...
# name Zain
# age Ninety
# gender male
# >>>
# >>> chai_types
# {'name': 'Zain', 'age': 'Ninety', 'gender': 'male'}
# >>> for key , value in chai_types.items():
# ...     print(key , value)
# ...
# name Zain
# age Ninety
# gender male
# >>>
# >>> if "gender" in chai_types:
# ...     print("I have Masala chai")
# ...
# I have Masala chai
# >>>
# >>> print(len(chai_types))
# 3
# >>>
# >>> chai_types
# {'name': 'Zain', 'age': 'Ninety', 'gender': 'male'}
# >>> chai_types["isMember"] = "True"
# >>> chai_types
# {'name': 'Zain', 'age': 'Ninety', 'gender': 'male', 'isMember': 'True'}
# >>>
# >>> chai_types.pop("gender")
# 'male'
# >>> chai_types
# {'name': 'Zain', 'age': 'Ninety', 'isMember': 'True'}
# >>>
# >>> chai_types.popitem()
# ('isMember', 'True')
# >>> chai_types
# {'name': 'Zain', 'age': 'Ninety'}
# >>>
#-----------------
# del : ye memory se pora reference delete karta hu .
# >>> chai_types
# {'name': 'Zain', 'age': 'Ninety'}
# >>> del chai_types["age"]
# >>> chai_types
# {'name': 'Zain'}
# >>>
# >>> chai_copy = chai_types.copy()
# >>> chai_copy
# {'name': 'Zain'}
# >>> chai_types
# {'name': 'Zain'}
# >>>
# >>> tea_shop = {
# ... "chai" : {"Masala": "Spicy", "Ginger": "Zesty"},
# ... "Tea" : {"Green": "Mild", "Black": "Strong"}
# ...
# ... }
# >>> tea_shop
# {'chai': {'Masala': 'Spicy', 'Ginger': 'Zesty'}, 'Tea': {'Green': 'Mild', 'Black': 'Strong'}}
# >>> tea_shop['chai']
# {'Masala': 'Spicy', 'Ginger': 'Zesty'}
# >>> tea_shop['chai']['Ginger']
# 'Zesty'
# >>>

# >>> squared_num = {x:x**2 for x in range(11)}
# >>> squared_num
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
# >>>
# >>> squared_num.clear()
# >>> squared_num
# {}
# >>>
# >>> keys
# >>> default_value = "Delicious"
# >>> new_dict = dict.fromkeys(keys , default_value)
# >>> new_dict
# {'Masala': 'Delicious', 'Ginger': 'Delicious', 'Lemon': 'Delicious'}
# >>> new_dict = dict.fromkeys(keys , default_value)
# >>> new_dict
# {'Masala': ('Spicy', 'strong', 'fresh'), 'Ginger': ('Spicy', 'strong', 'fresh'), 'Lemon': ('Spicy', 'strong', 'fresh')}      
# >>> new_dict = dict.fromkeys(keys , keys)
# >>> new_dict
# {'Masala': ['Masala', 'Ginger', 'Lemon'], 'Ginger': ['Masala', 'Ginger', 'Lemon'], 'Lemon': ['Masala', 'Ginger', 'Lemon']} 

# combine keys and values from zip method:
# Agar aap chahte hain ke har key ko list ke alag alag value assign ho, to aap **zip()** function use kar sakte hain. Misal ke taur par:

# ```python
# keys = ["Masala", "Ginger", "Lemon"]
# default_values = ["Spicy", "Strong", "Fresh"]
# new_dict = dict(zip(keys, default_values))
# print(new_dict)
# ```

# **Iska nateeja hoga:**

# ```python
# {'Masala': 'Spicy', 'Ginger': 'Strong', 'Lemon': 'Fresh'}
# ```

# **Aasaan Alfaaz Mein:**  
# - **zip()** function do lists ko pair karta hai.  
# - Pehli list ke har element ko, doosri list ke ussi position ke element se milata hai.  
# - Phir **dict()** in pairs ko ek dictionary bana deta hai.  

# Is tarah, har key ko alag value milti hai.

# >>> defualt_value = ["Spicy" , "Strong" , "Fresh"]
# >>> new_dict = dict(zip(keys, defualt_value))
# >>> new_dict
# {'Masala': 'Spicy', 'Ginger': 'Strong', 'Lemon': 'Fresh'}
# >>>

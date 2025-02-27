# Tuple is immutable : so its value cannot be changed.

# PS D:\python_revision\02_DataTypes> python
# Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> tea_types = ("Black" , "Green" , "Oolong")
# >>> tea_types
# ('Black', 'Green', 'Oolong')
# >>> tea_types[0]
# 'Black'
# >>> tea_types[-1]
# 'Oolong'
# >>> tea_types[1:]
# ('Green', 'Oolong')
# >>> tea_types[0]
# 'Black'
# >>> tea_types[0] = "Lemon"
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'tuple' object does not support item assignment
# >>>
# >>> len(tea_types)
# 3
# >>>
# >>> >>> tea_types
# ('Black', 'Green', 'Oolong')
# >>> more_tea = ("Herbal" , "Earl Grey")
# >>> all_tea = more_tea + tea_types
# >>> all_tea
# ('Herbal', 'Earl Grey', 'Black', 'Green', 'Oolong')
# >>>
# >>> if "Green" in all_tea:
# ...     print("I have Green Tea")
# ...
# I have Green Tea
# >>>
# >>> more_tea = ("Herbal" , "Earl Grey" , "Herbal")
# >>> more_tea.count("Herbal")
# 2
# >>>
# >>> more_tea.count("Herb")
# 0
# >>>
# >>> tea_types
# ('Black', 'Green', 'Oolong')
# >>> (black , green , oolong)  = tea_types
# >>> tea_types
# ('Black', 'Green', 'Oolong')
# >>> black --> its a variable
# 'Black'
# >>> green --> its a variable
# 'Green'
# >>> oolong --> its a variable
# 'Oolong'
# >>>
# >>> type(tea_types)
# <class 'tuple'>
# >>>
# >>> nest_tuple = ("Zain" , ("Sameer" , "Saim") , "Sarim")
# >>> nest_tuple
# ('Zain', ('Sameer', 'Saim'), 'Sarim')
# >>> nest_tuple[0]
# 'Zain'
# >>> nest_tuple[1]
# ('Sameer', 'Saim')
# >>> nest_tuple[1][0]
# 'Sameer'
# >>> nest_tuple[1][1]
# 'Saim'
# >>>

# PS D:\python_revision\02_DataTypes> python
# Type "help", "copyright", "credits" or "license" for more information.
# >>> ch
# >>> chai
# >>> print(chai)
# Lemon Chai
# >>> chai = "Masala Chai"
# >>> first_char = chai[0]
# >>> print(first_char)
# M
# >>> chai
# 'Masala Chai'
# >>> slice_chai = chai[:6]
# >>> slice
# slice_chai slice(
# >>> slice_chai
# 'Masala'
# >>> slice_chai = chai[-1]
# >>> slice_chai
# 'i'
# >>> num_list = "0123456789"
# >>> num_list[:]
# '0123456789'
# >>> num_list[3:]
# '3456789'
# >>> num_list[:7]
# '0123456'
# >>> num_list[0:7:2]
# '0246'
# >>> num_list[0:9:3]
# '036'
# >>>

# >>> >>> chai
# 'Masala Chai'
# >>> print(chai.lower())
# masala chai
# >>> print(chai.upper())
# MASALA CHAI
# >>> chai
# 'Masala Chai'
# >>>
# >>> chai = "   Masala Chai       "
# >>> chai
# '   Masala Chai       '
# >>> print(chai.strip())
# Masala Chai
# >>>
# >>> chai = "Lemon Chai"
# >>> print(chai.replace("Lemon" , "Ginger"))
# Ginger Chai
# >>> chai
# 'Lemon Chai'
# >>>
# >>> chai = "Lemon, Ginger, Mint, Masala"
# >>> chai
# 'Lemon, Ginger, Mint, Masala'
# >>> print(chai.split())
# ['Lemon,', 'Ginger,', 'Mint,', 'Masala']
# >>> print(chai.split(", "))
# ['Lemon', 'Ginger', 'Mint', 'Masala']
# >>
# >>> chai = "Masala Chai"
# >>> print(chai.find("Chai"))
# 7
# >>> print(chai.find("Chai"))
# 7
# >>> print(chai.find("chai"))
# -1  ka matlab value nahe mili 

# >>> chai_type = "Masala Chai"
# >>> chai_type = "Masala"
# >>> quantity = 2
# >>> order = "I ordered {} cups of {} chai"
# >>> order
# 'I ordered {} cups of {} chai'
# >>> print(order.format(quantity , chai_type))
# I ordered 2 cups of Masala chai
# >>>
# >>> chai_variety = ["Lemon" , "Ginger" , "Masala"]
# ['Lemon', 'Ginger', 'Masala']
# >>> print("".join(chai_variety))
# LemonGingerMasala
# >>> print(" ".join(chai_variety))
# Lemon Ginger Masala
# >>> print(", ".join(chai_variety))
# Lemon, Ginger, Masala
# >>> print("-".join(chai_variety))
# Lemon-Ginger-Masala
# >>>
# >>> chai
# 'Masala Chai'
# >>> for ch in chai:
# ...     print(ch)
# ...
# M
# a
# s
# a
# l
# a

# C
# h
# a
# i
# >>>
# >>> chai = "He said , \"Masala chai is awesome\" " 
# >>> chai
# 'He said , "Masala chai is awesome" '
# >>> / yani backslash ka matlab hai as it is print ho ga jo is ke ander hoga.
# >>>

# using Raw string :
# >>> chai = "Masala\nchai"
# >>> print(chai)
# Masala
# chai
# >>> chai = r"Masala\nchai"
# >>> print(chai)
# Masala\nchai
# >>> chai = r"c:\user\pwd\zain"
# >>> print(chai)
# c:\user\pwd\zain
# >>>

# >>> chai = "c:\user\pwd\zain"
#   File "<stdin>", line 1
#     chai = "c:\user\pwd\zain"
#            ^^^^^^^^^^^^^^^^^^
# SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \uXXXX escape
# >>> chai = "c:\\user\\pwd\\zain"
# >>> print(chai)
# c:\user\pwd\zain
# >>>
# >>> chai = "Masala Chai"
# >>> print("Masala" in chai)
# True
# >>> print("Masalaa" in chai)
# False
# >>>


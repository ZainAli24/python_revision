print("Hello from python and chai")


def chai(val):
    print(val)

chai("Lemon Tea")


chai_one = "Ginger Tea"
chai_two = "Mint Tea"
chai_three = "Masala chai"


# --------- Python Shell working ----------- #
# PS D:\python_revision\01_basics> python
# Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
# >>> score
# 500
# >>> tea
# NameError: name 'tea' is not defined
# >>> import os
# >>> os.getcwd()
# >>> for c in "ChaiCode":
#   File "<stdin>", line 2
#     for c in "ChaiCode":
#     ^
# >>> for c in "ChaiCode":
# ...     prcclsint()
# ...
#   File "<stdin>", line 2, in <module>
# ...     print(c)
# ...
# h
# a
# i
# >>> Fruits = ["Apple" , "Banana" , "Orange"]
# >>> for fruit in Fruits:
# ...     print(fruit)
# ...
# Apple
# Banana
# Orange
# >>> import sys
# >>> sys.plateform
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: module 'sys' has no attribute 'plateform'. Did you mean: 'platform'?
# >>> sys.platform
# 'win32'
# >>> ls
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'ls' is not defined. Did you mean: 'os'?
# Traceback (most recent call last):
# NameError: name 'die' is not defined. Did you mean: 'dir'?
# >>> dir
# <built-in function dir>
# >>>
# >>> dir()
# ['Fruits', '__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'c', 'fruit', 'os', 'score', 'sys']
# >>>

#------------------------------------------------------------------------------------------------#


# ----------Memory reference internal working(Mutable and ImmutableDataTypes) -------------------#
# PS D:\python_revision\01_basics> python
# Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> username = "ZainALI"
# >>> username
# 'ZainALI'
# >>> username = "Sammer"
# >>> username
# 'Sammer'
# >>> x = 10
# >>> x
# 10
# >>> y = x
# >>> y
# 10
# >>> x = 15
# >>> x
# 15
# >>> y
# 10
# >>> y = x
# >>> y
# 15
# >>>

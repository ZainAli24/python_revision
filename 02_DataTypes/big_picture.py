# --------- Numbers dataType -----------------#
# Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
# >>> 12+ 12
# >>> 12 * 15
# >>> 2.5 * 5
# >>> 2 ** 342

# >>> import math
# >>> math.pi
# 3.141592653589793
# >>> import random
# >>> random.random()
# 0.20291959776571855
# >>> random.random()
# 0.020728724141379717
# >>> random.choice([1 , 3 , 5 , 4 , 2])
# 3
# >>> random.choice([1 , 3 , 5 , 4 , 2])
# 5
# >>> random.choice([1 , 3 , 5 , 4 , 2])
# 5
# >>> random.choice([1 , 3 , 5 , 4 , 2])
# 4


# ------------- String Datatype -------------#
# >>> username = "chaiaurcode"
# >>> len(username)
# 11
# >>> username[2]
# 'a'
# >>> username[0] = 'A'
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'str' object does not support item assignment
# >>> username[0]
# 'c'
# >>> username[-1]
# 'e'
# >>> username[-2]
# 'd'
# >>> username[1:3]
# 'ha'
# >>> dir(username)
# ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
# >>>


# ---------------- List DataType -------------#
# >>> mylist = [123 , "Chai" , 3.14]
# >>> mylist
# [123, 'Chai', 3.14]
# >>> len(mylist)
# 3
# >>> mylist[0]
# 123
# >>> mylist[-1]
# 3.14
# >>> for item in mylist:
# ...     print(item)
# ...
# 123
# Chai
# 3.14
# >>>


# -----------Dictionary DataType -----------#
# >>> my_dict = {'name':'ZAIN' , 'age':21 , 'gender':'male'}
# >>> my_dict
# {'name': 'ZAIN', 'age': 21, 'gender': 'male'}
# >>> my_dict['gender']
# 'male'
# >>> my_dict['namer']
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# KeyError: 'namer'
# >>>



# ----------Tuple DataType ------------#
# >>> my_Tuple = (2 , 4 , 6 , 8)
# >>> my_Tuple
# (2, 4, 6, 8)
# >>> len(my_Tuple)
# 4
# >>> my_Tuple[3]
# 8
# >>> for tup in my
# mylist   my_dict  my_Tuple 
# >>> for tup in my_Tuple:
# ...     print(tup)
# ...
# 2
# 4
# 6
# 8
# >>>


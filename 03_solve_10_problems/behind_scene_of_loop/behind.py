# PS D:\python_revision\03_solve_10_problems\behind_scene_of_loop> python
# Type "help", "copyright", "credits" or "license" for more information.
# >>> file = open('chai.py')
# >>> file.readline()
# 'import time\n'
# >>> file.readline()
# 'print("Chai and Zain is here")\n'
# >>> file.readline()
# 'username = "ZAIN ALI"\n'
# >>> file.readline()
# 'print(username)\n'
# >>> file.readline()
# ''
# >>> file.readline()
# ''

# >>> file = open('chai.py')
# >>> file.__next__()
# 'import time\n'
# >>> file.__next__()
# 'print("Chai and Zain is here")\n'
# >>> file.__next__()
# 'username = "ZAIN ALI"\n'
# >>> file.__next__()
# 'print(username)\n'
# >>> file.__next__()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# StopIteration
# >>> file.__next__()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# StopIteration
# >>>

# >>> for line in open('chai.py'):
# ...     print(line)
# ...
# import time

# print("Chai and Zain is here")

# username = "ZAIN ALI"

# print(username)

# >>>
# >>> for line in open('chai.py'):
# ... for print(line , end="")
# ...
# import time
# print("Chai and Zain is here")
# username = "ZAIN ALI"
# print(username)
# >>>


# file = open('chai.py')
# while True:
#     line = file.readline()
#     if not line:
#         break
#     else:
#         print(line , end="")

# output is :
# import time
# print("Chai and Zain is here")
# username = "ZAIN ALI"
# print(username)

# not working:
# >>> test = "ZAIN"
# >>> if not test:
# ...     print("NOT")
# ...
# >>> test = ""
# >>> if not test:
# ...     print("Not")
# ...
# Not
# >>>

# list iteration:
# >>> my_list = [1, 2, 3, 4, 5]
# >>> I = iter(my_list)
# >>> I.__next__()
# 1
# >>> my_list = [1, 2, 3, 4, 5]
# >>> I = iter(my_list)
# >>> I
# <list_iterator object at 0x0000022C12B93070>
# >>> I.__next__()
# 1
# >>> I
# <list_iterator object at 0x0000022C12B93070>
# >>> I.__next__()
# 2
# >>> I.__next__()
# 3
# >>> I.__next__()
# 4
# >>> I.__next__()
# 5
# >>> I.__next__()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# StopIteration
# >>>

# iter in case of file:
# >>> file = open('chai.py')
# >>> file
# <_io.TextIOWrapper name='chai.py' mode='r' encoding='cp1252'>
# >>> iter(file) is file
# True
# >>> >>> file.__next__()
# 'import time\n'
# >>> file.__next__()
# 'print("Chai and Zain is here")\n'
# >>> file.__next__()
# 'username = "ZAIN ALI"\n'
# >>>

# iter in case of list:
# >>> mynewlist = [1, 2, 3]
# >>> iter(mynewlist) is mynewlist
# False
# >>>

# iter in case of Dictionary:
# >>> Dict = {'a': 1 , 'b': 2 , 'c': 3}
# >>> iter(Dict) is Dict
# False
# >>> I = iter(Dict)
# >>> I.__next__()
# 'a'
# >>> next(I)
# 'b'
# >>> next(I)
# 'c'
# >>> next(I)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# StopIteration
# >>>

# iter in case of range:
# >>> range(5)
# range(0, 5)
# >>> R = range(5)
# >>> R
# range(0, 5)
# >>> iter(R) is R
# False
# >>> I = iter(R)
# >>> I.__next__()
# 0
# >>> I.__next__()
# 1
# >>> I.__next__()
# 2
# >>> I.__next__()
# 3
# >>> I.__next__()
# 4
# >>> I.__next__()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# StopIteration
# >>>


# iter in case of string:
# >>> str = "abcdef"
# >>> iter(str) is str
# False
# >>> I = iter(str)
# >>> I.__next__()
# 'a'
# >>> I.__next__()
# 'b'
# >>> I.__next__()
# 'c'
# >>> I.__next__()
# 'd'
# >>> I.__next__()
# 'e'
# >>> I.__next__()
# 'f'
# >>> I.__next__()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# StopIteration
# >>>


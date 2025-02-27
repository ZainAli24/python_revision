# ----------memory references ----------#
# PS D:\python_revision\02_DataTypes> python
# Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> import sys
# >>> sys.getrefcount(24601)
# 3
# >>> sys.getrefcount('ZAIN')
# 4294967295
# >>> sys.getrefcount('Z')
# 4294967295
# >>> sys.getrefcount('2')
# 4294967295
# >>> sys.getrefcount(3)
# 4294967295
# >>>

# >>> a = 5
# >>> b = a
# >>> b
# 5
# >>> a = 15
# >>> b
# 5
# >>>


# >>> a = "ZAin"
# >>> a = 3.14
# >>> a
# 3.14
# >>> a = 5
# >>> b = 2
# >>> a = a + 2
# >>> a
# 7



# --------List Referece Deep ---------------#
# >>> mylistone = [1,2,3]
# >>> mylistTwo = mylistone
# >>> mylistone = [1,2,3]

# >>> mylistone
# [1, 2, 3]
# >>> mylistTwo
# [1, 2, 3]
# >>> mylistone = "Chai"
# >>> mylistone
# Chai
# >>> mylistTwo 
# [1 , 2 , 3]
# >>> mylistone = [1, 2, 3]
# >>> mylistTwo
# [1, 2, 3]
# >>> mylistone
# [1, 2, 3]

# >>> mylistone[0] = 42
# >>> mylistone
# [42, 2, 3]
# >>> mylistTwo
# [1, 2, 3]
# >>>


# ---Most important examlpe of memeory reference : 
# >>> L1 = [1 , 2 , 4]
# >>> L2 = L1
# >>> L1
# [1, 2, 4]
# >>> L2
# [1, 2, 4]
# >>> L1[0] = 11
# >>> L1
# [11, 2, 4]
# >>> L2
# [11, 2, 4]
# >>> P = [1 , 4 , 8]
# >>> Q = P
# >>> Q
# [1, 4, 8]
# >>> Q = [1 , 4 , 8]
# >>> P
# [1, 4, 8]
# >>> P[0] = 76
# >>> P
# [76, 4, 8]
# >>> Q
# [1, 4, 8]
# >>>


# ------most important deep in memeory reference -----------#
# >>> h1 = [1 , 4 , 5]
# >>> h2 = h1[:]      --> jab bhi hum slicing ya is tarah se reference dete hai toh us ki copy ban jati hai.
# >>> h1
# [1, 4, 5]
# >>> h2
# [1, 4, 5]
# >>> h1[0] = 66
# >>> h1
# [66, 4, 5]
# >>> h2
# [1, 4, 5]
# >>>

# >>> import copy
# >>> h2
# [1, 4, 5]
# >>> h2 = copy.copy(h2)  ye bhi same cheez hai woh slicing jesi.
# >>> h1
# [66, 4, 5]
# >>> h2 = copy.copy(h1)
# >>> h2
# [66, 4, 5]
# >>>

# copy.deepcopy(h5) --> is ka matlab hai ke list ke ander aghar ik aur list hai toh us ki copy.


# ---------- is and == in memory -------------#
# `==`: "Kya value same hai?"  
# `is`: "Kya dono variable ek hi object ko refer kar rahe hain?"

# >>> m = [1,2,3]
# >>> n = m
# >>> m
# [1, 2, 3]
# >>> n
# [1, 2, 3]
# >>> m == n
# True
# >>> n == m
# True
# >>> m is n
# True
# >>> n is m
# True
# >>> n = [1,2,3]
# >>> m == n
# True
# >>> m is n
# False
# >>> n is m
# False
# >>>

# ----------------------------------------------------------------------------#

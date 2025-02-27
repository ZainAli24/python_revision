# PS D:\python_revision\02_DataTypes> python
# Type "help", "copyright", "credits" or "license" for more information.
# >>> y = 5
# >>> x + y
# >>> x + (y * z)
# >>> 40 + 2.23
# 42.23
# >>> 'hitesh' + 3
# TypeError: can only concatenate str (not "int") to str
# 2
# 40.0
# 'chaiaurcode'
# (2, 5, 8)
# (5, 20)
# >>> y = 3
# >>> y % 2
# 1
# >>> z
# 8
# >>> z**2
# 64
# >>> x ** 4
# 16
# >>> z ** 4
# 4096
# >>> 100 ** 2
# 10000
# >>> 2 ** 100
# 1267650600228229401496703205376
# >>> 2 ** 1000
# 10715086071862673209484250490600018105614048117055336074437503883703510511249361224931983788156958581275946729175531468251871452856923140435984577574698574803934567774824230985421074605062371141877954182153046474983581941267398767559165543946077062914571196477686542167660429831652624386837205668069376
# >>> re
# return    result    repr(     reversed(
# >>> result
# 0.3333333333333333
# >>> repr('chai')
# "'chai'"
# >>> str('chai')
# 'chai'
# >>> print('chai')
# chai
# >>>
# >>> 1 < 2
# True
# >>>
# >>> 5.0 == 5.0
# True
# >>> 4.0 != 5.0
# True
# >>> x,y,z
# (2, 3, 8)
# >>> x < y < z
# True
# >>> x < y and y < z
# True
# >>> 1 == 2 < 3
# False
# >>> 1 == 2 and 2 < 3
# False
# >>>
# >>> import math
# >>> math.floor(3.5)
# 3
# >>> math.floor(-3.5)
# -4
# >>> math.floor(5.6)
# 5
# >>> math.floor(5.9)
# 5
# >>> math.trunc(2.8)
# 2
# >>> math.trunc(-2.8)
# -2
# >>>
# >>> 999999999999999999999999 + 1
# 1000000000000000000000000
# >>> 99999999999999999999999 * 2.1
# 2.0999999999999998e+23
# >>> 2 + 1j
# (2+1j)
# >>> (2 + 1j) * 3
# (6+3j)
# >>>
# >>> 0o20
# 16
# >>> 0xFF
# 255
# >>> 0b100
# 4
# >>> 0b1000
# 8
# >>> oct(64)
# '0o100'
# >>> hex(64)
# '0x40'
# >>> bin(64)
# '0b1000000'
# >>>
# >>> int(64)
# 64
# >>> int(64 , 8)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: int() can't convert non-string with explicit base
# >>> int('64' , 8)
# 52
# >>> int('64' , 16)
# 100
# >>> int('10000' , 2)
# 16
# >>> int('10000' , 4)
# 256
# >>>
# bitwise operations : 
# >>> x = 1
# >>> x << 2
# >>> 0b100
# 4
# >>> x = 2
# >>> x << 2
# 8
# >>> 0b200
#   File "<stdin>", line 1
#     0b200
#       ^
# SyntaxError: invalid digit '2' in binary literal
# >>>
# >>> 0b1000
# 8
#------------
# >>> >>> import random
# 0.979082485760509
# 0.575952720360253
# 0.1672036167689841
# 5
# 6
# 7
# 8
# 5
# 7
# 10
# 2
# 8
# 5
# 8
# 5
# 4
# 8
# 6
# >>> random.randint(1,11)
# 4
# >>> random.randint(1,11)
# 7
# >>> random.randint(1,11)
# 4
# >>> random.randint(1,11)
# 7
# >>> random.randint(1,11)
# 7
# >>>

# >>> li = ['Lemon' , 'Ginger' , 'Mint' , 'Masala']
# >>> random.choice(li)
# 'Ginger'
# >>> random.choice(li)
# 'Masala'
# >>> random.choice(li)
# 'Ginger'
# >>> random.choice(li)
# 'Mint'
# >>> random.choice(li)
# 'Lemon'
# >>>
# >>> random.shuffle(li)
# >>> li
# ['Lemon', 'Masala', 'Ginger', 'Mint']
# >>> random.shuffle(li)
# >>> li
# ['Masala', 'Ginger', 'Lemon', 'Mint']
# >>> random.shuffle(li)
# >>> li
# ['Mint', 'Ginger', 'Lemon', 'Masala']
# >>>
# "Shuffle" ka Urdu mein matlab hai **"بکھیرنا"** ya **"ملا دینا"**.  
# Yeh lafz aksar aise istimal hota hai jab cheezon ko mix karke unki order badal di jaye, jaise ke taash ko shuffle karna.



# Decimal:
# >>> 0.1 + 0.1 + 0.4
# 0.6000000000000001
# >>> 0.1 + 0.1 + 0.1
# 0.30000000000000004
# >>> 0.1 + 0.1 + 0.1 - 0.3
# 5.551115123125783e-17
# >>> (0.1 + 0.1 + 0.1) - 0.3
# 5.551115123125783e-17
# >>>______ from decimal import Decimal ________
# >>> Decimal('0.1') + Decimal('0.1') + Decimal('0.1')
# Decimal('0.3')
# >>> Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3')
# Decimal('0.0')
# >>>

# ------Union and intersection in sets --------- :
# >>> setone = {1,2,3,4}
# >>> setTwo = {5,4,3}
# >>> setone | setTwo
# {1, 2, 3, 4, 5}
# >>> setone & setTwo
# {3, 4}
# >>> setone - {1 , 2 , 3 ,4}
# set()
# >>> type({})
# <class 'dict'>

# >>> >>> type(True)
# <class 'bool'>
# >>> True == 1
# True
# >>> False == 0
# True
# >>>
# >>> True is 1
# False
# >>> True + 4
# 5

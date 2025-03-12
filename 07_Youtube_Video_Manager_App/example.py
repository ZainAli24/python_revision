# enumerate working:
x = ('Masala', 'Ginger', 'Lemon')

y = enumerate(x)
print(y)
print(dict(y))

print(list(y))

y = enumerate(x)
print(list(y))

y = enumerate(x)
print(tuple(y))


#----------------------------------------------------------------------------------------------------

# File handling in python

# 1. read mode: aghar hum file ko read mode mein open kar rahe hai toh hamre pass wo file mojood honi chahiye, aghar wo file mojood nahe hai toh error ae ga.
file = open('zain.txt', 'r')  

# 2. write mode: aghar hum file ko write mode mein open kar rahe hai toh hamre pass aghar wo file mojood nahe hai toh wo automatically write mode mien open ho jae gi.
file = open('zain.txt', 'w')  

# - write mode with try, finally: is case mein hum ko file ko khud close karna hota hai.
file = open('zain.txt', 'w')  

try:
    file.write("ZAIN Aur Cohort")
finally:
    file.close()

# - write mode using (with) : is case mein hum ko file ko khud close nahe karna hota hai, wo khud close ho jati hai
with open('zain.txt', 'w') as file:
    file.write("Zain aur chai")

# 6. Lambda Function
# Problem: Create a lambda function to compute the cube of a number.

cube = lambda val: val ** 3

print(cube(2))
res = cube(3)
print(res)

anotherCub = cube
print(anotherCub(5))

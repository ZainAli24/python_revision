# ex : 1
username = "ZAIN ALI"
def func():
    # username = "Sameer"
    print(username)


print(username)
func()


# ex : 2
x = 89

def func2(y):
    z = x + y
    return z

res = func2(1)
print(res)


# ex : 3
def func3():
    global x
    x = 20
   
func3()
print(x)


# ex : 4
def nest():
    x = 70
    def f1():
        print(x)
    f1()

nest()


## Closure:
def closure():
    x = 44
    def inner():
        print(f"val = {x}")
    return inner

res = closure()
res()


## Proper Closure or Factory functions:
def closure2(num):
    def actual(x):
        return x ** num
    return actual

res = closure2(2)
print(res(3))
res2 = closure2(3)
print(res2(3))


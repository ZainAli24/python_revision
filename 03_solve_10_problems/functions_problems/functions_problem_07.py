# ▼7. Function with *args
# Problem: Write a function that takes variable number of arguments and returns their sum.

# def args(*args):
#     return sum(args)


# print(args(4 , 6 , 20))
# res = args(5 , 15 , 25)
# print(res)


# 2.
def args2(*chai):
    print(chai)
    for i in chai:
        print(i * 2)
    return f"Sum is {sum(chai)}"


print(args2(3, 5, 6, 7))    

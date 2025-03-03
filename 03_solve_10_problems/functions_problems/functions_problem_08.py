# 8. Function with **kwargs
# Problem: Create a function that accepts any number of keyword arguments and prints them in the format
# key: value

def kwargs(**kwargs):
    print(kwargs)
    for key, val in kwargs.items():
        print(f"{key}: {val}")
    

kwargs(username="ZAIN" , age= 20)

